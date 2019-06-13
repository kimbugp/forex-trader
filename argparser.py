import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--start_date",
                    type=lambda d: datetime.strptime(d, '%Y-%m-%d'),
                    help='Start date of data - format YYYY-MM-DD')

parser.add_argument("--end_date",
                    type=lambda d: datetime.strptime(d,
                                                     '%Y-%m-%d'),
                    help='End date of data - format YYYY-MM-DD')

parser.add_argument("--currency_pair",
                    type=str,
                    help='Currency paid')

args = parser.parse_args()
