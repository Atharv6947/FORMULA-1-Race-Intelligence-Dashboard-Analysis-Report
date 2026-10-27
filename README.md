# FORMULA-1-Race-Intelligence-Dashboard-Analysis-Report
Formula 1 data analysis using Tableau to visualize driver performance, constructor standings, tyre strategies, podiums, and race reliability through interactive dashboards and data-driven insights.
# 🏎️ Formula 1 Race Intelligence Analysis — Tableau Dashboard

## 📌 Project Overview

The **Formula 1 Race Intelligence Analysis** project uses Tableau to explore Formula 1 racing data and uncover insights into driver performance, team championship standings, tyre strategies, podium achievements, circuit characteristics, and race reliability.

The project transforms raw racing data into interactive visualisations and dashboards to help users identify performance trends, compare teams and drivers, analyse race outcomes, and understand the factors associated with Did Not Finish (DNF) results.

The analysis is designed around three real-world scenarios involving an F1 team performance strategist, a motorsport broadcast analyst, and a technical regulation analyst.

## 🎯 Project Objectives

- Analyse constructor and driver performance across seasons.
- Compare team championship points and identify performance trends.
- Explore tyre compound usage across different circuit types.
- Identify leading drivers based on points and laps led.
- Determine which countries host the most Grand Prix races.
- Analyse podium finishes by driver and team.
- Investigate DNF causes and their distribution across constructors.
- Examine DNF patterns across circuits and seasons.
- Evaluate driver race completion rates over time.
- Present the findings through interactive Tableau dashboards.

## 📊 Dataset Description

The project uses the **F1 Racing Project Dataset**, provided in Excel format.

The workbook contains five sheets:

| Sheet Name | Description |
|---|---|
| `race_results` | Race-level driver results, points, teams, circuit details, tyre strategies, and DNF information. |
| `championship_standings` | Driver standings, championship points, wins, podiums, pole positions, and DNFs by season. |
| `lap_intelligence` | Lap times, sector times, tyre compounds, tyre age, DRS activity, and speed-trap information. |
| `qualifying_results` | Qualifying positions, lap times, tyre compounds, and qualifying performance metrics. |
| `circuits` | Circuit names, countries, cities, circuit types, lap distances, altitude, and direction. |

### Key dataset fields

The analysis uses fields such as:

- **Performance:** `driver`, `team`, `points`, `wins`, `podiums`, `laps_led`
- **Season and race:** `season`, `race_id`, `round`, `race_date`
- **Circuit information:** `circuit_name`, `country`, `city`, `circuit_type`
- **Tyre strategy:** `starting_compound`, `tyre_strategy`, `tyre_compound`
- **Reliability:** `dnf`, `dnf_reason`, `finish_position`
- **Lap performance:** `lap_time_s`, `sector1_s`, `sector2_s`, `sector3_s`

The `race_results` sheet contains 6,464 records.

## 📈 Visualisations

The project is organised into nine visualisations covering the three analysis scenarios.

| No. | Visualisation | Chart Type | Scenario |
|---|---|---|---|
| 1 | Constructor Championship Points by Season | Line Chart | Team Performance |
| 2 | Starting Tyre Compound by Circuit Type | Stacked Bar Chart | Team Performance |
| 3 | Driver Performance by Total Laps Led | Bar Chart | Team Performance |
| 4 | Driver Performance Leaderboard | Horizontal Bar Chart | Broadcast Analysis |
| 5 | Grand Prix Races by Host Country | Bar Chart | Broadcast Analysis |
| 6 | Podium Finishes by Driver and Team | Stacked Bar Chart | Broadcast Analysis |
| 7 | DNF Causes by Constructor | Stacked Bar Chart | Technical Reliability |
| 8 | DNF Count by Circuit and Season | Heatmap | Technical Reliability |
| 9 | Driver Non-DNF Rate by Season | Line Chart | Technical Reliability |

### Scenario 1: F1 Team Performance Strategist

This scenario focuses on evaluating constructor performance, comparing championship points, examining tyre compound usage, and identifying drivers who contribute strongly to race performance.

### Scenario 2: Motorsport Broadcast Analyst

This scenario focuses on identifying leading drivers, ranking Grand Prix host countries, and analysing podium achievements to support motorsport reporting and broadcast visualisations.

### Scenario 3: Technical Regulation Analyst

This scenario focuses on understanding DNF reasons, identifying patterns across circuits and constructors, and examining changes in race completion rates over time.

## 🛠️ Tools and Technologies

- **Tableau Desktop / Tableau Public** — Data visualisation and dashboard development
- **Microsoft Excel** — Dataset storage and preliminary data inspection
- **GitHub** — Project documentation and version control

## 🚀 How to Use the Project

1. Clone or download this repository.
2. Download and install Tableau Desktop or Tableau Public.
3. Open the Tableau workbook (`.twb` or `.twbx`) included in the repository.
4. If Tableau cannot locate the original Excel data source, reconnect it to the included dataset.
5. Open the worksheets to explore individual visualisations.
6. Open the dashboard to view the combined analysis.
7. Interact with available filters and chart selections to explore different seasons, teams, drivers, and race outcomes.

**Note:** A `.twb` file stores workbook definitions but may refer to an external dataset. Include the Excel dataset in the repository and update the data-source path if necessary. A `.twbx` packaged workbook can simplify sharing by including supported local data files.

## 💡 Key Analytical Measures

The project explores several important Formula 1 performance measures:

- **Championship points:** Points accumulated by drivers or teams.
- **Podium finishes:** Results in first, second, or third position.
- **Tyre compound usage:** Recorded starting compounds and tyre strategy patterns.
- **DNF count:** Number of race-result records marked as Did Not Finish.
- **DNF rate:** Percentage of eligible race-result records marked as DNF.
- **Non-DNF rate:** Percentage of records not marked as DNF.
- **Laps led:** Total laps led by each driver.

These measures help compare performance, explore reliability patterns, and identify areas for further investigation.

## ⚠️ Data and Interpretation Notes

- The supplied dataset does not contain a driver nationality field. Nationality-based comparisons require an additional driver nationality dataset.
- Tyre compound usage in `race_results` is based on recorded starting compounds and strategies; detailed tyre stint analysis can use `lap_intelligence`.
- DNF counts and DNF rates are different measures. Rates are generally more suitable for comparing reliability when participation varies.
- A non-DNF result is not necessarily proof of complete race distance or mechanical reliability.
- Championship points and performance measures should be interpreted in the context of the seasons and scoring systems represented in the data.
- Findings depend on the completeness, consistency, and accuracy of the supplied dataset.

## 📌 Project Outcome

The project demonstrates how Tableau can be used to transform Formula 1 racing data into interactive visualisations that support performance benchmarking, race strategy exploration, broadcast analysis, and reliability investigation.

The resulting dashboard provides a consolidated view of racing performance and helps users explore patterns across drivers, constructors, circuits, seasons, and race outcomes.

## 👤 Author

**Author:** [Atharv Pagar]

**Project:** Formula 1 Race Intelligence Analysis

**Technology:** Tableau

---

*This project was developed for data visualisation and analytical learning purposes.*
