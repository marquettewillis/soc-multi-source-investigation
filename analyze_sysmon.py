import csv
from pathlib import Path

csv_file = Path.home() / "Downloads" / "04_Splunk_PowerShell_Process_Evidence.csv"

with csv_file.open(newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for event in reader:
        print(event["CommandLine"])