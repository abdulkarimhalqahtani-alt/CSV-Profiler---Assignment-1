# CSV Profiler

A modular Python tool to analyze CSV files and generate basic statistics.
This version reflects Assignment 2, where the code was refactored into a
package with separated responsibilities.

## Features
- Counts number of rows
- Lists column names
- Calculates basic statistics:
  - Non-empty values per column
  - Unique values per column
- Generates output reports in JSON and Markdown formats

## Project Structure
csv-profiler/
├── data/
│   └── sample.csv
├── outputs/
│   ├── report.json
│   └── report.md
├── src/
│   ├── csv_profiler/
│   │   ├── __init__.py
│   │   ├── io.py
│   │   ├── profile.py
│   │   └── render.py
│   └── main.py
├── README.md

## How to Run
Make sure you are in the project root directory, then run:

```bash
python src/main.py
