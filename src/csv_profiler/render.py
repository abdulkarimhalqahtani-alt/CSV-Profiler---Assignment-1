def render_markdown(report):
    lines = []
    lines.append("# CSV Profile Report\n")
    lines.append(f"- Rows: {report['rows']}")
    lines.append(f"- Columns: {', '.join(report['columns'])}\n")
    lines.append("## Column Stats")

    for col, stats in report["stats"].items():
        lines.append(
            f"- *{col}*: non-empty={stats['non_empty']}, unique={stats['unique']}"
        )

    return "\n".join(lines)
