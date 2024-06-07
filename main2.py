import argparse
from datetime import datetime
import sys

sys.path.append('/Users/albertgrayce01/PycharmProjects/Проект 1/venv')
from fetch_stock_data import fetch_stock_data


def validate_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_string}. Expected format: YYYY-MM-DD.")


def main():
    parser = argparse.ArgumentParser(description='Stock data fetcher.')
    parser.add_argument('--start_date', type=validate_date, required=True, help='Start date in YYYY-MM-DD format.')
    parser.add_argument('--end_date', type=validate_date, required=True, help='End date in YYYY-MM-DD format.')

    args = parser.parse_args()

    start_date = args.start_date
    end_date = args.end_date

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    data = fetch_stock_data(start_date_str, end_date_str)
    print(data)


if __name__ == '__main__':
    main()
