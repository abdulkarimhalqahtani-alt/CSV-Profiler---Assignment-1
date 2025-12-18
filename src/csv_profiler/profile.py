def profile_csv(rows):
    row_count = len(rows)
    columns = rows[0].keys() if rows else []

    column_stats = {}
    for col in columns:
        values = [row[col] for row in rows if row[col] != ""]
        column_stats[col] = {
            "non_empty": len(values),
            "unique": len(set(values)),
        }

    report = {
        "rows": row_count,
        "columns": list(columns),
        "stats": column_stats,
    }

    return report
