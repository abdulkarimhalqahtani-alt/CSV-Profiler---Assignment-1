from profiler import profile_csv

def main():
    input_path = "data/sample.csv"
    output_json = "outputs/report.json"
    output_md = "outputs/report.md"

    profile_csv(input_path, output_json, output_md)

if __name__ == "__main__":
    main()