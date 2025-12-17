import csv
import json
from collections import Counter


def profile_csv(input_path, output_json, output_md):
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    row_count = len(rows)
    columns = reader.fieldnames

    column_stats = {}
    for col in columns:
        values = [row[col] for row in rows if row[col] != ""]
        column_stats[col] = {
            "non_empty": len(values),
            "unique": len(set(values)),
        }

    report = {
        "rows": row_count,
        "columns": columns,
        "stats": column_stats,
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# CSV Profile Report\n\n")
        f.write(f"- Rows: {row_count}\n")
        f.write(f"- Columns: {', '.join(columns)}\n\n")
        f.write("## Column Stats\n")
        for col, stats in column_stats.items():
            f.write(
                f"- *{col}*: non-empty={stats['non_empty']}, unique={stats['unique']}\n"
            )