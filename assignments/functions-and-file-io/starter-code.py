from pathlib import Path

PASSING_SCORE = 70
DATA_FILE = Path("grades.csv")
REPORT_FILE = Path("report.txt")


def load_grades(file_path):
    """Load grade rows from CSV and return a list of (name, score) tuples."""
    # TODO: Open the file and parse lines.
    # Expected format per row: name,score
    # Skip the header and any malformed rows.
    pass


def calculate_stats(records):
    """Return a dictionary with average, highest, lowest, and passing_count."""
    # TODO: Compute stats from parsed records.
    # If records is empty, return zeros for all values.
    pass


def format_report(stats):
    """Create a human-readable report string from the stats dictionary."""
    # TODO: Build and return a multi-line string report.
    pass


def write_report(file_path, report_text):
    """Write the final report text to disk."""
    # TODO: Write report_text into file_path.
    pass


def main():
    records = load_grades(DATA_FILE)
    stats = calculate_stats(records)
    report_text = format_report(stats)
    write_report(REPORT_FILE, report_text)
    print("Report generated:", REPORT_FILE)


if __name__ == "__main__":
    main()
