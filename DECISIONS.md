# Decisions

Newest first. One entry per decision taken at a stop point.

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
