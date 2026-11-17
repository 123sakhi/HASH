"""Checks for the baseline model (output of 2_BaselineModel/baseline-model.ipynb).

Sources of truth: the prepared table (ids, rows per period), the split definition (B1)
and the metrics recomputed independently from the saved validation predictions.

Run from the repository root with:  uv run pytest checks/
"""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
PREPARED = ROOT / "0_DataPreparation" / "prepared_data.csv"
OUT = ROOT / "2_BaselineModel"
VALID_START, VALID_END = pd.Timestamp("2017-08-01"), pd.Timestamp("2018-07-31")


def _read(name):
    path = OUT / name
    assert path.exists(), f"{path} not found: run the baseline notebook first"
    return pd.read_csv(path, parse_dates=["Datum"])


@pytest.fixture(scope="module")
def prepared():
    return pd.read_csv(PREPARED, parse_dates=["Datum"])


@pytest.fixture(scope="module")
def valid():
    return _read("validation_predictions.csv")


@pytest.fixture(scope="module")
def test_pred():
    return _read("predictions_test.csv")


def test_validation_rows_are_the_validation_year(prepared, valid):
    """B1: validation = every training row from 2017-08-01 to 2018-07-31, nothing else."""
    expected = prepared[(prepared["set"] == "train") & prepared["Datum"].between(VALID_START, VALID_END)]
    assert sorted(valid["id"]) == sorted(expected["id"])
    assert valid["Datum"].min() == VALID_START and valid["Datum"].max() == VALID_END


def test_validation_turnover_unchanged(prepared, valid):
    m = valid.merge(prepared[["id", "Umsatz"]], on="id", suffixes=("", "_prepared"))
    assert len(m) == len(valid)
    assert np.allclose(m["Umsatz"], m["Umsatz_prepared"])


def test_validation_predictions_complete_and_positive(valid):
    for col in ["pred_baseline", "pred_naive"]:
        assert valid[col].notna().all(), f"{col} has missing values"
        assert (valid[col] > 0).all(), f"{col} has non-positive values"


def test_metrics_reproduce(valid):
    """The saved metrics equal MAPE/MAE recomputed here from the saved predictions."""
    metrics = pd.read_csv(OUT / "validation_metrics.csv")
    for model, col in [("baseline", "pred_baseline"), ("naive", "pred_naive")]:
        for group, g in valid.groupby("Warengruppe"):
            row = metrics[(metrics["model"] == model) & (metrics["Warengruppe"] == group)]
            assert len(row) == 1
            mape = (np.abs(g[col] - g["Umsatz"]) / g["Umsatz"]).mean() * 100
            mae = np.abs(g[col] - g["Umsatz"]).mean()
            assert np.isclose(row["MAPE"].iloc[0], mape)
            assert np.isclose(row["MAE"].iloc[0], mae)


def test_test_predictions_match_prepared_ids(prepared, test_pred):
    expected = prepared.loc[prepared["set"] == "test", "id"]
    assert list(test_pred["id"]) == list(expected)


def test_test_predictions_plausible(prepared, test_pred):
    assert test_pred["Umsatz_pred"].notna().all()
    assert (test_pred["Umsatz_pred"] > 0).all()
    max_train = prepared.loc[prepared["set"] == "train", "Umsatz"].max()
    assert test_pred["Umsatz_pred"].max() < 3 * max_train
