# 📘 Assignment: Functions and File I/O

## 🎯 Objective

Build a small gradebook processor in Python by writing reusable functions, reading CSV data from a file, and generating a clear summary report.

## 📝 Tasks

### 🛠️\tRead and Parse Grade Data

#### Description
Write functions that load student grade records from a CSV file and convert each row into usable Python data.

#### Requirements
Completed program should:

- Read from `grades.csv` using Python file I/O.
- Skip the header row and parse each record into structured data (name, score).
- Validate score values as numbers and ignore malformed rows safely.

### 🛠️\tAnalyze and Report Results

#### Description
Use separate functions to calculate class statistics and write a summary report to a new text file.

#### Requirements
Completed program should:

- Compute at least: class average, highest score, lowest score, and number of passing students.
- Define and use a `PASSING_SCORE` constant.
- Save a human-readable report to `report.txt`.
