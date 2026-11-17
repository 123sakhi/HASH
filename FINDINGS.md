# Findings

What we have learned so far, in plain words. The **overview** at the top is kept short and updated each week. The **detailed notes** at the bottom keep every number and are never rewritten: each week adds a new section there.

All effects are in **turnover** (sales amount), not pieces. Numbers come from `1_DatasetCharacteristics/week-03-factors.ipynb`.

---

## 1. Where we are

| Step | What it means | Status |
|---|---|---|
| Project setup | Repository, canvas, glossary, decision log | ✅ Done |
| Week 1: Seasonal bread | When and how much seasonal bread sells | ✅ Done |
| Week 2: Weekdays | How sales differ Monday to Sunday | ✅ Done |
| Week 3: Weather, Kiel Week, holidays | Do these change sales, and by how much? | ✅ Done |
| Project question (`/grill-question`) | What we forecast, for whom, how we judge it | ✅ Done (Q1–Q11), team to confirm |
| Data preparation (`0_DataPreparation`) | Clean notebook that merges and prepares the data | ⏳ Next |
| Baseline model (`2_BaselineModel`) | Simple linear regression to beat | ⬜ Not started |
| Main model (`3_Model`) | Neural network, tuning, MAPE per product group | ⬜ Not started |
| Presentation (`4_Presentation`) | Slides, 8–10 minutes | ⬜ Not started |

---

## 2. Our questions and answers

### The project question (decided with `/grill-question`, details in `DECISIONS.md`)

| # | Question | Our answer |
|---|---|---|
| Q1 | Who decides what, and when? | The branch's operations manager decides once a day (about 14:00–15:00) how much of each of the six product groups to bake tomorrow. |
| Q2 | What do we forecast? | **Turnover** per product group for tomorrow, not pieces (the data has no prices or piece counts). |
| Q3 | Which factors do we study? | Weekday, season and holidays, weather, Kiel Week. All four change the plan. |
| Q4 | What happens today without a model? | Assumed: same weekday last week, plus experience. *To confirm with the client.* |
| Q5 | Who gets which result? | Manager: daily table with a range. Technical reader: notebooks and a model card. Course: slides. |
| Q6 | How do we measure error? | MAPE per product group (course metric), plus MAE to show the real size of errors. |
| Q7 | What must the model beat? | "Same weekday last week" first, then the course's linear regression. |
| Q8 | Which mistake costs more? | For bread, rolls and croissants, baking too little is assumed worse. *To confirm with the client.* |
| Q9 | Which days must be good? | Weekends, Kiel Week, 24 and 31 December, the seasonal bread season. Reported separately. |
| Q10 | Can we use weather? | Yes, observed weather, labelled as a best case (only a forecast is known in reality). Also tested without weather. |
| Q11 | Which past sales may the model use? | Only up to yesterday. In the Kaggle test year, sales are withheld, so no recent sales there. |

### The analysis questions (answered by the data)

| Question | Short answer | How sure? |
|---|---|---|
| **(a) Do weekdays matter?** | **Yes, a lot.** Monday–Friday is flat. Weekends are much higher for rolls (Sun +48 %), croissants (Sun +42 %) and confectionery (Sun +69 %). Bread is the exception: **Sunday −40 %**. | Strong |
| **(b) Do season and holidays matter?** | **Yes, very much.** Seasonal bread climbs from ~35 a day (late Oct) to ~90 (early Dec). The shop is closed on 25/26 Dec and 1 Jan. 24 and 31 Dec are busy for bread and rolls. **Cakes on 31 Dec are about 7× a normal day.** | Strong for the patterns, but only 5 years of each holiday |
| **(c) Does weather matter?** | **A little.** Warmer days: rolls up (+0.6 % per °C), cakes down (−0.7 % per °C). More clouds slightly lower rolls, croissants and cakes. Bread is not affected. | Weak for most groups; effects are small |
| **(d) Does Kiel Week matter?** | **Yes, for rolls (+21 %) and croissants (+26 %).** Smaller for bread (+10 %) and cakes (+8 %). | Clear effect, but only 5 Kiel Weeks |

---

## 3. What each week found (short version)

- **Week 1 – Seasonal bread:** It is sold only from late October to early January. Demand builds up and jumps in late November (in all 5 seasons), peaks in early December, then drops. The start date differs by year.
- **Week 2 – Weekdays:** Monday to Friday look alike (within about ±8 %). Saturday and Sunday are busier for everything except bread, which drops by 40 % on Sundays.
- **Week 3 – Weather, Kiel Week, holidays:** Weather has only small effects. Kiel Week clearly boosts rolls and croissants. Christmas and New Year have the biggest effects of all, especially cakes on 31 December.

**What this means for the model:** weekday, holidays (with special handling for 24/31 Dec and closed days), Kiel Week and the seasonal bread season should go in. Weather is worth testing but adds little.

---

## 4. Still open

| Open question | Who resolves it |
|---|---|
| Price data, to turn turnover into pieces | Team, if the bakery can provide it |
| Exact decision time, and how the manager decides today | Client |
| Is baking too little really worse than too much? | Client |
| Opening hours on Sundays and holidays | Client |
| What causes the cakes peak on 31 December (doughnuts? pre-orders?) | Client |
| Easter, Pentecost, other holidays and school holidays: not checked yet | Team, later week |
| One model with recent sales (real use) and one without (Kaggle), or only one? | Team, when building the model |
| One Kiel Week effect for all groups, or one per group? | Team, when building the model |

---

<details>
<summary><b>Detailed notes (all numbers, unchanged weekly sections) – click to open</b></summary>

### Summary table

Effect = change in average daily turnover. Weekday effects are vs. the Monday–Friday average. Weather and Kiel Week effects come from a regression that holds weekday, month and year constant. Holiday effects are vs. other December/January days. "Use in model?" is a **draft for the team to confirm**.

| Factor | Product group | Effect (plain words) | Evidence | Source | Use in model? |
|---|---|---|---|---|---|
| Weekday | Bread | Saturday +17 %, **Sunday −40 %** (Sunday lower in 98 % of weeks) | strong | week-03-factors, Week 3 (re-check of Week 2) | yes |
| Weekday | Rolls | Saturday +33 %, Sunday +48 % | strong | week-03-factors, Week 3 | yes |
| Weekday | Croissants | Saturday +37 %, Sunday +42 % | strong | week-03-factors, Week 3 | yes |
| Weekday | Confectionery | Saturday +9 % (higher in only 60 % of weeks), Sunday +69 % | strong (Sun) / weak (Sat) | week-03-factors, Week 3 | yes |
| Weekday | Cakes | Saturday +19 %, Sunday +18 % | strong | week-03-factors, Week 3 | yes |
| Weekday | Seasonal bread | Saturday +14 %, Sunday −9 % (about 40 weeks only) | weak | week-03-factors, Week 3 | test |
| Season | Seasonal bread | Builds through the season: ~35 late Oct → ~90 early Dec per day; late November +26 % to +116 % vs early November in all 5 seasons | strong (late-Nov jump) | week-03-factors, Week 3 (re-check of Week 1) | yes |
| Season | Seasonal bread | November +70 % vs October | weak (only 13 October days in 3 seasons; one season goes the other way) | week-03-factors, Week 3 | test |
| Temperature | Bread | no clear effect (−0.2 % per °C, could be 0) | none | week-03-factors, Week 3 | no |
| Temperature | Rolls | +0.6 % per °C | weak | week-03-factors, Week 3 | test |
| Temperature | Croissants | +0.5 % per °C (borderline) | weak | week-03-factors, Week 3 | test |
| Temperature | Confectionery | −0.5 % per °C (borderline) | weak | week-03-factors, Week 3 | test |
| Temperature | Cakes | −0.7 % per °C | strong | week-03-factors, Week 3 | test |
| Temperature | Seasonal bread | −2.6 % per °C (282 days only) | weak | week-03-factors, Week 3 | test |
| Cloud cover | Bread, Confectionery | no clear effect | none | week-03-factors, Week 3 | no |
| Cloud cover | Rolls, Croissants, Cakes | −0.4 % to −0.8 % per octa more cloud | weak to strong (small effect) | week-03-factors, Week 3 | test |
| Cloud cover | Seasonal bread | −3.4 % per octa | weak (282 days) | week-03-factors, Week 3 | test |
| Kiel Week | Bread | +10 % on Kiel Week days | weak (5 Kiel Weeks) | week-03-factors, Week 3 | test |
| Kiel Week | Rolls | **+21 %** | strong effect, but only 5 Kiel Weeks | week-03-factors, Week 3 | yes |
| Kiel Week | Croissants | **+26 %** | strong effect, but only 5 Kiel Weeks | week-03-factors, Week 3 | yes |
| Kiel Week | Confectionery | +7 %, could be 0 | none | week-03-factors, Week 3 | no |
| Kiel Week | Cakes | +8 % | weak (5 Kiel Weeks) | week-03-factors, Week 3 | test |
| Kiel Week | Seasonal bread | not measurable (not sold in June) | none | week-03-factors, Week 3 | no |
| Holidays | All groups | 25 Dec, 26 Dec, 1 Jan: no sales in any year (shop presumably closed) | strong | week-03-factors, Week 3 | yes |
| Holidays | Bread, Rolls | 24 Dec +99 % / +55 %; 31 Dec +120 % / +93 % | weak (5 years each) | week-03-factors, Week 3 | yes |
| Holidays | Croissants | 24 Dec +16 %, 31 Dec +65 % | weak (5 years) | week-03-factors, Week 3 | test |
| Holidays | Cakes | **31 Dec about 7× a normal day (+627 %; +511 % to +702 % every year)**; 24 Dec +4 % | strong (all 5 years) | week-03-factors, Week 3 | yes |
| Holidays | Confectionery, Seasonal bread | 31 Dec −43 % / −45 % (sold in only 2 / 1 years) | weak | week-03-factors, Week 3 | test |

### Week 1

*Original analysis is not in this repository (probably in `ml-practice`). The numbers below were re-computed in `1_DatasetCharacteristics/week-03-factors.ipynb`, section 2.*

- **Seasonal bread demand builds through the season.** Average daily turnover rises from about 35 (late October) to 44 (early November), 73 (late November) and 90 (early December), then falls to 68 (late December) and 31 (early January). *How sure:* clear pattern over 5 seasons. *Does not tell us:* why. It could be demand, or a bigger range on display.
- **Jump in late November.** 16–30 November is +26 % to +116 % above 1–15 November, in **all 5 seasons**. *How sure:* strong in direction, but the size varies a lot between seasons.
- **October vs November test:** November is +70 % above October (Welch t-test, p < 0.001). *How sure:* **weak**. There are only 13 October days, all in late October, from 3 seasons, and in 2017/18 November was *lower* than October (−22 %). The p-value counts days, but the independent cases are seasons. *Does not tell us:* what happens in early October. In 2015 and 2016 sales only started in early November.
- **The season length differs by year:** it starts between 24 October and 3 November and ends between 27 December and 6 January. *Does not tell us:* whether the start date is a decision by the bakery (supply) or a reaction to demand.

### Week 2

*Original analysis is not in this repository. The numbers below were re-computed in `1_DatasetCharacteristics/week-03-factors.ipynb`, section 3.*

- **Weekend effect for most groups.** Compared with the Monday–Friday average, Saturday and Sunday are higher for Rolls (+33 % / +48 %), Croissants (+37 % / +42 %) and Cakes (+19 % / +18 %). Confectionery peaks on Sunday (+69 %). *How sure:* strong. Sunday is higher than that week's Monday–Friday average in 93–97 % of about 260 weeks for Rolls, Croissants and Confectionery.
- **Sunday bread is low:** Bread on Sunday is −40 % (median −40 %). It is higher than Monday–Friday in only 2 % of weeks. *How sure:* strong. Saturday bread is +17 %.
- **Monday to Friday is flat:** all groups stay within about ±8 % of their Monday–Friday average.
- **Seasonal bread:** Saturday +14 %, Sunday −9 %. *How sure:* weak, with only about 40 weeks of data.
- *Does not tell us:* whether the Sunday pattern comes from shorter opening hours or from demand. The data has no opening hours.

### Week 3

*Notebook: `1_DatasetCharacteristics/week-03-factors.ipynb`, sections 4–5. We merged sales, weather and Kiel Week on the date, and the row count stayed 9,334. Model: log(turnover) ~ temperature + cloud cover + Kiel Week + weekday + month + year, one per product group, with HAC (7-day) standard errors. 9,264 rows were used; 70 rows without weather were dropped.*

- **Kiel Week matters most for Rolls (+21 %, 95 % range +16 % to +26 %) and Croissants (+26 %, +19 % to +34 %).** Bread is +10 % and Cakes +8 %. Confectionery is not clear. *How sure:* the effects are large, but they rest on **only 5 Kiel Weeks (45 days)**. *Does not tell us:* whether a future Kiel Week will look the same, for example with different weather or event size.
- **Weather effects are small.** Per +1 °C (within the same month): Cakes −0.7 %, Rolls +0.6 %, Croissants +0.5 %, Confectionery −0.5 %, Bread no clear effect. More cloud lowers Rolls, Croissants and Cakes slightly (−0.4 % to −0.8 % per octa). Seasonal bread shows −2.6 % per °C and −3.4 % per octa, but from only 282 days. *How sure:* **weak** for most groups. For example, a 10 °C swing changes Cakes by only about 7 %. *Does not tell us:* how well a weather **forecast** works. These are observed weather values, and at 14:00 the day before only a forecast is available.
- **Christmas and New Year:** there are no sales on 25 Dec, 26 Dec or 1 Jan in any year. 24 Dec and 31 Dec are busy for Bread (+99 % / +120 %) and Rolls (+55 % / +93 %). *How sure:* weak (5 years each), but the same direction every year.
- **Cakes on 31 December are about 7 times a normal December/January day** (+627 % on average; between +511 % and +702 % in every one of the 5 years). *How sure:* strong and consistent. *Does not tell us:* which product causes it (possibly New Year's Eve doughnuts; ask the client). It is a single day per year, so the model needs a special rule or a feature for it.
- *General limit:* all effects are in turnover, not pieces. Price changes between 2013 and 2018 are hidden inside the year effect.

### Open questions

- **Price data** per product group, to convert turnover into pieces and to separate price changes from demand. *Resolves:* team, by asking the client.
- **Opening hours** on Sundays and holidays (24 Dec, 31 Dec; closed 25/26 Dec and 1 Jan?). *Resolves:* client.
- **What drives the 31 December cakes peak** (special product such as doughnuts?), and is it pre-ordered? *Resolves:* client.
- **Seasonal bread season start:** does the bakery decide when it starts, and when? *Resolves:* client.
- **Weather forecast vs observed weather:** can we get historical forecasts, or do we accept observed weather as an upper bound? *Resolves:* team (canvas block 6).
- **Kiel Week:** with only 5 events, should the model use one Kiel Week effect for all groups or one per group? *Resolves:* team, when building the model.
- **Holidays not yet checked:** Easter, Pentecost, other public holidays and school holidays. *Resolves:* team, in a later week.

</details>
