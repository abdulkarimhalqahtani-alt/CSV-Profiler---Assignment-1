from csv_profiler.io import read_csv, write_json
from csv_profiler.profile import profile_csv
from csv_profiler.render import render_markdown


def main():
    input_path = "data/sample.csv"
    output_json = "outputs/report.json"
    output_md = "outputs/report.md"

    rows = read_csv(input_path)
    report = profile_csv(rows)

    write_json(report, output_json)

    md = render_markdown(report)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md)


if __name__ == "__main__":
    main()
