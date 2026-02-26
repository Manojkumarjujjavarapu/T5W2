import argparse
import os
from src.report_service import ReportService


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input folder path")
    parser.add_argument("--output", required=True, help="Output folder path")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    service = ReportService(args.input, args.output)
    service.generate_report()


if __name__ == "__main__":
    main()