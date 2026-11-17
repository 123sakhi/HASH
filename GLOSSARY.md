# Glossary

One entry per term, variable or code the project uses. Keep the canonical name, the meaning, the unit and anything that is easy to get wrong.

| Term | Meaning | Unit / values | Notes |
|---|---|---|---|
| Warengruppe (product group) | Product category of the bakery branch | 1 Bread, 2 Rolls, 3 Croissants, 4 Confectionery, 5 Cakes, 6 Seasonal bread | Group 6 only sold October–January; group 4 has no rows on 53 days |
| Umsatz (turnover) | Turnover of one product group on one day; target variable in the data | Money amount, currency not stated | Turnover, not number of pieces baked or sold |
| Decision time | Moment the next day's baking quantities are fixed | Daily, about 14:00–15:00 the day before | Team assumption, not confirmed by the client |
| MAPE (mean absolute percentage error) | Average of \|forecast − actual\| / actual, per product group | % | Main metric (course/Kaggle). Exaggerates errors on small values, e.g. seasonal bread |
| MAE (mean absolute error) | Average of \|forecast − actual\|, per product group | Turnover units | Reported next to MAPE to show the real size of errors |
| Naive baseline | Forecast = turnover of the same product group on the same weekday one week earlier | Turnover | Minimum bar a model must beat; needs recent sales, so not computable in the Kaggle test year |
| Known in advance | Information available at decision time (14:00 the day before) | — | Calendar, Kiel Week, weather forecast, sales up to yesterday. Anything else used as a feature is leakage |
| Leakage | Information the model would not have at decision time that still reaches training or evaluation | — | Makes results look better than they will be in use |
| Observed weather | Weather that actually happened on the day (`wetter.csv`) | °C, octas, m/s, WMO code | Not a forecast; results using it are a best case |
| Lag feature | A past value of turnover used as input, e.g. turnover 7 days earlier | Turnover | Only from yesterday or earlier; not available in the Kaggle test year |
| Kaggle test year | Period whose sales are withheld for the course competition | 2018-08-01 to 2019-07-31 | Weather and Kiel Week available, sales not |
