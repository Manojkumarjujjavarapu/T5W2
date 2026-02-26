GitHub Repository Link:

https://github.com/Manojkumarjujjavarapu/T5W2.git


# Batch Report Generator

## Project Overview

The Batch Report Generator is a Python-based automation tool designed to process student data from multiple CSV sources and generate a clean, consolidated report for training teams.

Training data often comes from different systems such as marks, attendance, and submissions, which may contain missing values, duplicate entries, or inconsistent formats. This project reads such data, performs cleaning, and produces structured outputs for analysis and reporting.

The system uses **Pandas for data processing**, **Object-Oriented Programming (OOP)** for modular design, and **exception handling** for robustness.

---

## Features

* Reads multiple CSV files from an input folder
* Handles missing values and duplicate records
* Converts numeric fields into proper data types
* Merges datasets into a single student report
* Generates:

  * Per-student report (CSV)
  * Batch summary metrics (JSON)
* Implements OOP using a `ReportService` class
* Graceful error handling if files are missing
* Command-line execution support


## Project Structure

PY2_BATCH_REPORT_GENERATOR/
│
├── input_data/
│   ├── students.csv
│   └── attendance.csv
│
├── output/
│
├── src/
│   └── report_service.py
│
├── main.py
├── requirements.txt
└── README.md


## Input Files

Place input files inside the `input_data` folder.

### students.csv

Required columns:

studentId, name, marks


Example:

1, Manoj, 85
2, Kumar, 60


### attendance.csv

Required columns:


studentId, attendancePercent


Example:


1, 90
2, 75


## Output Files Generated

After execution, the system creates the following files inside the `output` folder:

### 1️ report.csv

Per-student summary containing:

* studentId
* name
* marks
* attendancePercent
* status (PASS / FAIL)

### 2️ summary.json

Overall batch metrics including:

* totalStudents
* avgAttendance
* avgMarks
* passCount
* failCount
* top3Students


##  How to Run

Install dependencies:


pip install -r requirements.txt


Run the project:


python main.py --input input_data --output output

## ⚙️ Processing Logic

The system performs the following steps:

1. Load CSV files from the input directory
2. Remove duplicate rows
3. Handle missing values by replacing with default values
4. Convert numeric columns into proper data types
5. Merge datasets using studentId
6. Calculate pass/fail status based on marks
7. Generate report and summary outputs



## Error Handling

If any required file is missing, the program will display a clear error message and exit gracefully without crashing.


## Technologies Used

* Python
* Pandas
* NumPy
* JSON
* argparse (CLI support)



##  Generated Files


output/report.csv  
output/summary.json


------>   Manoj Kumar Jujjavarapu