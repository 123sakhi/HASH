# Experiment log

One entry per run that counts. Never delete entries; mark superseded ones.

<!--
## YYYY-MM-DD: <card id> <short title>
**Change vs. previous best:** <one line>
**Data / features:** <version or commit>
**Config / seed(s):** <...>
**Validation result:** <metric overall> (baseline: <metric>)
**By segment:** <metric per relevant group>
**Checks:** all passing / <which failed>
**Verdict:** adopted / rejected / inconclusive, with reason
**Commit:** <sha>
-->

## 2026-11-17: baseline-lr Linear regression per product group
**Change vs. previous best:** first model; compared with the naive baseline "same weekday last week".
**Data / features:** `0_DataPreparation/prepared_data.csv`; weekday, month, Kiel Week, holiday, day before holiday, 24 Dec, 31 Dec, temperature, cloud cover, wind, precipitation. Target: log(turnover).
**Config / seed(s):** scikit-learn `LinearRegression`, one model per product group; deterministic (no seed). Fit 2013-07-01 to 2017-07-31, validation 2017-08-01 to 2018-07-31.
**Validation result:** MAPE all groups 19.3 % (naive: 22.4 %).
**By segment:** MAPE regression / naive: Bread 17.5 / 26.5, Rolls 16.2 / 13.7, Croissants 19.2 / 21.4, Confectionery 23.3 / 26.4, Cakes 16.1 / 19.9, Seasonal bread 46.3 / 48.4. Kiel Week 19.1 / 25.1 (9 days); 24 and 31 Dec 45.8 / 35.5 (2 days); weekends 20.5 / 21.8.
**Checks:** all passing (18, `uv run pytest checks/`).
**Verdict:** adopted as baseline. Beats the naive forecast for 5 of 6 groups; **not for rolls**.
**Commit:** see `git log -- 2_BaselineModel` (same commit as this entry).
