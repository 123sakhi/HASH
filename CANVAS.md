# Agentic Data Science Canvas

**Project:** HASH: bakery sales forecast
**Team:** Hanif Ahmed Sakhi, Afifa Khalid, Huie Feng, Saikiran Panchireddi
**Version:** 2026-11-17

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
<!-- Who decides what, when and how often? What happens today without this analysis? -->
- **Who:** the branch's operations manager decides; the head baker carries out the plan. Head office is not involved in daily quantities.
- **What:** one quantity per product group (all six groups) for the whole next day.
- **When / how often:** once per day, in the afternoon (about 14:00–15:00) for the next day, so the night shift can start baking in the evening.
- **Assumption:** the exact time is the team's estimate; the client has not specified it (see Open questions).
- **Today without this analysis:** assumed: the manager bakes roughly what sold on the same weekday last week, adjusted by experience. Team assumption, to confirm with the client (see Open questions).

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
- **Main question:** How much turnover will each of the six product groups make tomorrow?
  - *Data can answer:* daily turnover per product group, 2013-07-01 to 2018-07-31.
  - *Data cannot answer:* number of pieces (no prices, no piece counts); unsold or sold-out goods (only actual sales are recorded, not quantities baked). Price changes over 2013–2019 may shift turnover patterns without any change in demand.
  - The operations manager converts the turnover forecast into pieces using current prices and experience.
- **Sub-questions (all four change the plan; evidence in `FINDINGS.md`):**
  - (a) **Weekday:** how much does turnover differ Monday to Sunday per group? Strong effect (e.g. Sunday bread −40 %, Sunday rolls +48 %).
  - (b) **Season and holidays:** summer vs. winter, seasonal bread season, Christmas/New Year. Very large effects (e.g. cakes on 31 Dec about 7× a normal day), but *data cannot answer reliably:* only ~5 occurrences per holiday; Easter, Pentecost and school holidays not yet checked.
  - (c) **Weather:** do temperature and cloud cover change turnover? Small effects in opposite directions (warmer: rolls +0.6 % per °C, cakes −0.7 % per °C). *Data cannot answer:* effect of a weather **forecast**, which is all that is known at decision time.
  - (d) **Kiel Week:** extra turnover during Kiel Week? Strong for rolls (+21 %) and croissants (+26 %). *Data cannot answer reliably:* only 5 Kiel Weeks.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->
- **Operations manager (decision-maker):** a daily table, one row per product group, with the forecast turnover and a range ("between X and Y") that shows how sure the forecast is.
- **Technical reader (course instructors, other teams):** notebooks that run top to bottom, plus a short model report (model card).
- **Course presentation:** slides in `4_Presentation`.

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->
- **Metric:** MAPE per product group (main metric, the course grades on it), plus MAE per product group, because MAPE exaggerates errors on small values (e.g. seasonal bread).
- **Baselines to beat:** (1) "same weekday last week" as the minimum bar; (2) the course's linear regression as the next step. A model that does not beat (1) is not worth using.
  - Limit: in the Kaggle test year no recent sales are available, so (1) can only be scored on our own validation period, not on Kaggle (see block 6).
- **Costlier errors:** depends on the product group. For fresh daily goods (bread, rolls, croissants) baking too little is assumed worse than too much. MAPE treats both directions equally, so this shapes how we read and present results, not the training. Client to confirm.
- **Segments reported separately:** weekends, Kiel Week, 24 and 31 December, the seasonal bread season. Limit: only ~5 Kiel Weeks and ~5 New Year's Eves, so these scores are noisy.

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->
- **Moment:** about 14:00 the day before the forecast day.
- **Known then:** calendar (date, weekday, month, holidays), Kiel Week dates, a weather *forecast* for tomorrow, and sales **up to and including yesterday**.
- **Not known then:** today's complete sales, tomorrow's actual weather, tomorrow's sales of any product group.
- **Weather:** our data has only observed weather. We use it and label results as a **best case** (a real forecast is less accurate), and also run the model without weather to see what weather adds at most.
- **Kaggle test year (2018-08-01 to 2019-07-31):** sales are withheld, so recent-sales features (lags) are not available there. A Kaggle model can only use calendar, Kiel Week and weather, or sales from before 2018-08-01. Our own validation must follow the same rule if we want its score to predict the Kaggle score.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->
See `FINDINGS.md` (running log, one section per week, with a summary table per factor and product group).

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it. -->
- Price data per product group, to convert turnover into pieces (later improvement). Resolves: team, if the bakery can provide it.
- Exact time of the daily baking decision (assumed 14:00–15:00 the day before). Resolves: team, ideally confirmed with the client.
- How the manager decides today (assumed: same weekday last week plus experience). Resolves: client.
- Whether baking too little is really worse than too much, and for which groups. Resolves: client.
- Recent-sales features: build two model versions (with lags for real use, without lags for Kaggle) or only the Kaggle-compatible one? Resolves: team, when building the model.

## Decision log
See `DECISIONS.md`.
