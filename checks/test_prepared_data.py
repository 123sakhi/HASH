"""Checks for the prepared data table (output of 0_DataPreparation/data-preparation.ipynb).

Each check compares the prepared table with a source of truth the notebook did not compute:
the raw files, the calendar, or the key definition (one row per date and product group).

Run from the repository root with:  uv run pytest checks/
"""

from pathlib import Path

import pandas as pd
import pytest

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"
PREPARED = Path(__file__).resolve().parents[1] / "0_DataPreparation" / "prepared_data.csv"

FEATURES = [
    "weekday", "weekday_num", "month", "KielerWoche", "is_holiday", "day_before_holiday",
    "christmas_eve", "new_years_eve", "seasonal_bread_season",
    "Temperatur", "Bewoelkung", "Windgeschwindigkeit", "weather_filled", "precipitation", "temp_band",
]


@pytest.fixture(scope="module")
def prepared():
    assert PREPARED.exists(), f"{PREPARED} not found: run the data preparation notebook first"
    return pd.read_csv(PREPARED, parse_dates=["Datum"])


@pytest.fixture(scope="module")
def raw_sales():
    return pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv", parse_dates=["Datum"])


def test_training_rows_equal_raw_sales(prepared, raw_sales):
    """D1: training rows are exactly the raw sales rows, nothing added or lost."""
    train = prepared[prepared["set"] == "train"]
    assert len(train) == len(raw_sales)
    merged = raw_sales.merge(train, on=["Datum", "Warengruppe"], suffixes=("_raw", ""))
    assert len(merged) == len(raw_sales)
    assert (merged["Umsatz_raw"] - merged["Umsatz"]).abs().max() < 1e-9
    assert (merged["id_raw"] == merged["id"]).all()


def test_one_row_per_date_and_group(prepared):
    assert not prepared.duplicated(["Datum", "Warengruppe"]).any()
    assert prepared["id"].is_unique


def test_date_ranges(prepared):
    train = prepared[prepared["set"] == "train"]
    test = prepared[prepared["set"] == "test"]
    assert train["Datum"].min() == pd.Timestamp("2013-07-01")
    assert train["Datum"].max() == pd.Timestamp("2018-07-31")
    assert test["Datum"].min() == pd.Timestamp("2018-08-01")
    assert test["Datum"].max() == pd.Timestamp("2019-07-31")
    assert set(prepared["set"]) == {"train", "test"}


def test_test_year_covers_every_day(prepared):
    """D6: every day of the Kaggle test year is present for product groups 1-5."""
    test = prepared[prepared["set"] == "test"]
    days = pd.date_range("2018-08-01", "2019-07-31")
    for group in range(1, 6):
        assert len(test[test["Warengruppe"] == group]) == len(days)


def test_id_matches_date_and_group(prepared):
    expected = prepared["Datum"].dt.strftime("%y%m%d") + prepared["Warengruppe"].astype(str)
    assert (prepared["id"].astype(str) == expected).all()


def test_no_missing_features(prepared):
    assert not prepared[FEATURES].isna().any().any(), prepared[FEATURES].isna().sum()


def test_turnover(prepared):
    train = prepared[prepared["set"] == "train"]
    test = prepared[prepared["set"] == "test"]
    assert (train["Umsatz"] > 0).all()
    assert test["Umsatz"].isna().all()


def test_weekday_matches_calendar(prepared):
    assert (prepared["weekday_num"] == prepared["Datum"].dt.dayofweek).all()
    assert (prepared["weekday"] == prepared["Datum"].dt.day_name()).all()


def test_kiel_week_matches_raw_file(prepared):
    kiwo = pd.read_csv(BASE_URL + "kiwo.csv", parse_dates=["Datum"])
    flagged = set(prepared.loc[prepared["KielerWoche"] == 1, "Datum"])
    in_range = set(kiwo["Datum"]) & set(prepared["Datum"])
    assert flagged == in_range


def test_weather_in_plausible_range(prepared):
    assert prepared["Temperatur"].between(-30, 45).all()
    assert prepared["Bewoelkung"].between(0, 8).all()
    assert (prepared["Windgeschwindigkeit"] >= 0).all()


def test_special_days(prepared):
    d = prepared["Datum"]
    assert (prepared["christmas_eve"] == ((d.dt.month == 12) & (d.dt.day == 24)).astype(int)).all()
    assert (prepared["new_years_eve"] == ((d.dt.month == 12) & (d.dt.day == 31)).astype(int)).all()
