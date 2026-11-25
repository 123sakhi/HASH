# Decisions

Newest first. One entry per decision taken at a stop point.

## 2026-11-17: Baseline model setup (B1–B6)
**Canvas block:** 9
**Decision:**
- B1: train 2013-07-01 to 2017-07-31, validate 2017-08-01 to 2018-07-31; split by time, never shuffled.
- B2: one linear regression per product group.
- B3: predict log(turnover), convert back with exp.
- B4: features weekday, month, Kiel Week, holiday, day before holiday, 24 Dec, 31 Dec, temperature, cloud cover, wind, precipitation. No temperature band (repeats temperature), no seasonal bread flag (repeats month), no holiday type (training holiday rows are all open days).
- B5: no trend over the years.
- B6: after validation, retrain on all training data and predict the Kaggle test year (`2_BaselineModel/predictions_test.csv`).
**Reason:** The validation year mirrors the Kaggle test year (B1). Weekday effects differ in direction between groups (B2). Our effects are percentages, and MAPE is relative (B3). A straight-line trend would continue the 2013–2017 decline although 2017/18 rose again (B5).
**Alternatives considered:** B1 random split (leakage); B2 one model for all groups; B3 turnover directly; B5 linear trend.
**Decided by:** Team HASH ("all as recommended").

## 2026-11-17: Data preparation rules (D1–D7)
**Canvas block:** 7
**Decision:**
- D1: keep only existing sales rows; do not fill missing date/group combinations with 0.
- D2: fill missing temperature, cloud cover and wind by interpolation between neighbouring days; flag them with `weather_filled`.
- D3: `precipitation` = 1 for weather codes 50–99; a missing code counts as no precipitation.
- D4: add Schleswig-Holstein public holidays (package `holidays`), the day before a holiday, 24 Dec and 31 Dec. School holidays later.
- D5: features as listed on the canvas (block 7); no lag features yet.
- D6: build the same features for the Kaggle test year, with empty turnover.
- D7: save `0_DataPreparation/prepared_data.csv`; add checks in `checks/test_prepared_data.py`.
**Reason:** A missing row means not sold or closed, not zero demand (D1). Only 26 days of weather need filling (D2). The dataset documentation says a missing code most likely means no notable weather (D3). Holidays have the largest effects in `FINDINGS.md` (D4). The same preparation for training and Kaggle avoids mismatches (D6).
**Alternatives considered:** D1 fill with 0; D2 drop rows; D3 keep raw codes or drop them; D4 no holidays or school holidays now; D6 build test features later.
**Decided by:** Team HASH ("all as recommended"). Temperature band cut points (10 and 20 °C) are a draft for the team to check.

## 2026-11-17: Recent sales only up to yesterday
**Canvas block:** 6
**Decision:** Features may use sales up to and including yesterday, never today's or later sales.
**Reason:** At 14:00 the day before, today's sales are not complete; using them would be leakage.
**Alternatives considered:** (b) Sales up to today: leakage. (c) No recent sales at all: needed for the Kaggle test year anyway, because its sales are withheld; whether to build both versions is an open question.
**Decided by:** Team HASH (Q11 of /grill-question). Fact checked: the course data withholds sales for 2018-08-01 to 2019-07-31.

## 2026-11-17: Use observed weather as a best case
**Canvas block:** 6
**Decision:** Use the observed weather in `wetter.csv`, label results as a best case, and also run the model without weather.
**Reason:** Only a weather forecast is known at decision time, but no historical forecasts are available. Weather effects are small (FINDINGS, Week 3), so the gap is probably small; the comparison without weather shows what weather adds at most.
**Alternatives considered:** (b) Drop weather: loses small but real effects for rolls and cakes. (c) Find historical forecasts: costly; not available now.
**Decided by:** Team HASH (Q10 of /grill-question).

## 2026-11-17: Report special segments separately
**Canvas block:** 4
**Decision:** Next to the overall MAPE, report scores for weekends, Kiel Week, 24 and 31 December, and the seasonal bread season.
**Reason:** These are the days with the largest effects, where mistakes cost most.
**Alternatives considered:** Overall score only: hides failures on the most important days.
**Decided by:** Team HASH (Q9 of /grill-question). Limit: about 5 Kiel Weeks and 5 New Year's Eves, so segment scores are noisy.

## 2026-11-17: Costlier errors depend on the product group
**Canvas block:** 4
**Decision:** For fresh daily goods (bread, rolls, croissants), baking too little is assumed worse than too much; for other groups no assumption is made. This shapes how results are read and presented, not the training metric.
**Reason:** Empty shelves lose customers; MAPE treats both directions equally.
**Alternatives considered:** (a) Both errors cost the same; (b) too little is always worse.
**Decided by:** Team HASH (Q8 of /grill-question). To confirm with the client.

## 2026-11-17: Baselines to beat
**Canvas block:** 4
**Decision:** Minimum bar: "same weekday last week". Next step: the course's linear regression.
**Reason:** If a model cannot beat the simplest believable rule, it is not worth using.
**Alternatives considered:** Average for the same weekday and month in past years: kept as a possible extra comparison.
**Decided by:** Team HASH (Q7 of /grill-question). Limit: the naive baseline needs last week's sales, so it can only be scored on our own validation period, not in the Kaggle test year.

## 2026-11-17: MAPE plus MAE per product group
**Canvas block:** 4
**Decision:** MAPE per product group is the main metric; MAE per product group is reported next to it.
**Reason:** The course grades on MAPE; MAPE exaggerates errors on small values, MAE shows their real size.
**Alternatives considered:** MAPE only; another metric.
**Decided by:** Team HASH (Q6 of /grill-question).

## 2026-11-17: Audiences and formats
**Canvas block:** 3
**Decision:** Operations manager: daily table per product group with a forecast range. Technical reader: notebooks plus a model card. Course: slides in `4_Presentation`.
**Reason:** The range shows how sure the forecast is, which matters on holidays and Kiel Week.
**Alternatives considered:** A table without a range.
**Decided by:** Team HASH (Q5 of /grill-question).

## 2026-11-17: Current practice assumed to be "same weekday last week"
**Canvas block:** 1
**Decision:** Assume the manager today bakes roughly what sold on the same weekday last week, adjusted by experience.
**Reason:** Simplest believable rule; it also serves as the baseline in block 4.
**Alternatives considered:** Gut feeling only; a fixed standard plan; unknown.
**Decided by:** Team HASH (Q4 of /grill-question). Assumption, to confirm with the client.

## 2026-11-17: Four sub-questions: weekday, season and holidays, weather, Kiel Week
**Canvas block:** 2
**Decision:** Keep all four factors as sub-questions: weekday, season and holidays, weather, Kiel Week.
**Reason:** All four change the plan. Weekday and Kiel Week effects are strong; weather works in opposite directions for rolls and cakes; holidays have very large effects but only a few days of data (see `FINDINGS.md`, Week 3).
**Alternatives considered:** Dropping weather (small effects) or holidays (few cases): rejected, both change the plan for some product groups.
**Decided by:** Team HASH (Q3 of /grill-question).

## 2026-11-17: Forecast turnover, not pieces
**Canvas block:** 2
**Decision:** Forecast turnover per product group for tomorrow. The operations manager converts it into pieces using current prices and experience.
**Reason:** Turnover is what the data contains; there are no prices or piece counts.
**Alternatives considered:** (b) Treat turnover as pieces: rejected, a price change would look like a change in demand. (c) Get price data to convert to pieces: not available now; a useful later improvement if the bakery can provide it.
**Decided by:** Team HASH (Q2 of /grill-question). Limitation noted: forecast is in turnover, and price changes over 2013–2019 may affect the patterns.

## 2026-11-17: The decision the project supports
**Canvas block:** 1
**Decision:** The branch's operations manager decides once per day, around 14:00–15:00, how much of each of the six product groups to bake for the whole next day; the head baker carries out the plan.
**Reason:** The data is daily per product group, and the night shift needs the plan before it starts baking in the evening.
**Alternatives considered:** Head baker or head office decides; decision late in the evening; several decisions per day. Not chosen: head office is not involved in daily quantities, and the night shift needs the plan earlier.
**Decided by:** Team HASH (Q1 of /grill-question). The exact time is an assumption, see Open questions on the canvas.




<!--
## YYYY-MM-DD: <short title>
**Canvas block:** <number>
**Decision:** <what was decided>
**Reason:** <why>
**Alternatives considered:** <what else, and why not>
**Decided by:** <names>
-->
