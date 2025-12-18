import csv
import json


def read_csv(input_path):
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_json(report, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
