"""Starter check: the main sales dataset can be loaded.

Run all checks from the repository root with:  uv run pytest checks/
"""

import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/opencampus-sh/intro-to-data-science-and-ml/main/data/bakery/"


def test_sales_data_loads():
    sales = pd.read_csv(BASE_URL + "umsatzdaten_gekuerzt.csv")
    assert len(sales) > 0, "sales file is empty"
    for column in ["Datum", "Warengruppe", "Umsatz"]:
        assert column in sales.columns, f"missing column {column}"
