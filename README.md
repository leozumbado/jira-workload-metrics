# Jira Ticket Workload Metrics

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This project is a lightweight data pipeline built in Python to analyze Jira ticket workloads and generate weekly operational metrics.

The pipeline processes exported Jira ticket data (CSV format), filters relevant tickets, classifies them by due date into weekly categories, and calculates workload metrics per producer.

The purpose of this project is to demonstrate practical skills in **data processing, transformation, and metric calculation using Python and Pandas**, following a modular and maintainable pipeline structure.

---

## Business Problem

Engineering teams often need visibility into upcoming workload in order to properly distribute tasks and avoid bottlenecks.

However, Jira exports typically contain raw ticket data that requires manual analysis.

This project automates that analysis by:

* Processing exported ticket datasets
* Identifying tickets due in the current and next week
* Calculating workload distribution across producers

The result is a simple but effective way to understand **short-term workload and team capacity**.

---

## Features

* Load multiple CSV datasets exported from Jira
* Filter only open tickets
* Normalize ticket labels to identify producers
* Classify tickets by time horizon:

  * This Week
  * Next Week
  * Later
* Calculate key operational metrics:

  * Tickets due this week
  * Tickets due next week
  * Average weekly workload per producer

---

## Tech Stack

* Python 3
* pandas
* NumPy
* Git
* GitHub

---

## Project Structure

```
jira-workload-metrics/
│
├── data/
│   └── *.csv                # Jira exported datasets
│
├── scripts/
│   ├── load_data.py         # Load and combine CSV datasets
│   ├── transform_data.py    # Data cleaning and transformations
│   ├── calculate_metrics.py # Workload metrics calculations
│
├── main.py                  # Pipeline execution script
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Pipeline Architecture

The data pipeline follows a modular structure where each stage has a specific responsibility.

```
CSV Data
   │
   ▼
load_data.py
   │
   ▼
transform_data.py
   │
   ├─ filter_open_tickets
   ├─ classify_tickets_by_week
   └─ classify_tickets_by_labels
   │
   ▼
calculate_metrics.py
   │
   ▼
main.py
   │
   ▼
Weekly Workload Metrics
```

This structure keeps the pipeline **modular, reusable, and easy to maintain**.

---

## Example Dataset

Example structure of a Jira CSV export:

| Ticket ID | Status | Labels | Due Date   |
| --------- | ------ | ------ | ---------- |
| T-101     | Open   | c-lz   | 2026-03-15 |
| T-102     | Open   | c-sr   | 2026-03-18 |
| T-103     | Done   | c-lz   | 2026-03-12 |

Labels are normalized during processing to identify the ticket owner.

---

## Example Output

```
Tickets This Week: 3
Tickets Next Week: 4

Average Workload Per Producer:

  Labels  avg_weekly_workload
0   lz    1.67
1   sr    1.33
```

This output provides quick insight into current and upcoming workload distribution.

---

## How to Run the Project

Clone the repository:

```
git clone https://github.com/leozumbado/jira-workload-metrics
cd jira-workload-metrics
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python main.py
```

---

## Future Improvements

Potential improvements for the project include:

* Export metrics to JSON or CSV
* Add workload visualizations
* Generate automated weekly reports
* Integrate directly with the Jira API instead of CSV exports
* Build a small dashboard for monitoring ticket workload

---

## Author

Leonardo J. Zumbado
Computer Science / Software Engineer

This project is part of my data engineering and analytics portfolio.
