import typer
from csv_profiler.io import read_csv, write_json
from csv_profiler.profile import profile_csv
from csv_profiler.render import render_markdown

app = typer.Typer()


@app.command()
def main(
    input_path: str,
    out: str = "outputs"
):
    """
    CSV Profiler CLI
    """
    rows = read_csv(input_path)
    report = profile_csv(rows)

    json_path = f"{out}/report.json"
    md_path = f"{out}/report.md"

    write_json(report, json_path)

    md = render_markdown(report)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    typer.echo("✅ Report generated successfully")


if __name__ == "__main__":
    app()
