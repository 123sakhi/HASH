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
- **Today without this analysis:** not yet discussed.

### 2. Questions 👤
<!-- The analysis questions that would change the decision. For each: what the data can answer, and what it cannot. -->
- **Main question:** How much turnover will each of the six product groups make tomorrow?
  - *Data can answer:* daily turnover per product group, 2013-07-01 to 2018-07-31.
  - *Data cannot answer:* number of pieces (no prices, no piece counts); unsold or sold-out goods (only actual sales are recorded, not quantities baked). Price changes over 2013–2019 may shift turnover patterns without any change in demand.
  - The operations manager converts the turnover forecast into pieces using current prices and experience.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->

---

## Data and method

### 5. Data 🤖
<!-- Sources, unit of observation, period covered, keys, known gaps. Link the data fact sheet. -->

### 6. Known in advance 👤
<!-- What information is available at the moment the result is needed? Everything else is leakage. -->

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

## Decision log
See `DECISIONS.md`.
