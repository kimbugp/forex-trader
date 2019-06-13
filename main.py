import sys
from datetime import datetime

import click

from currency_pairs import CURRENCY_OPTIONS, SOURCES
from data_plotter import Plot


@click.command()
@click.option("--start_date",
              type=lambda d: datetime.strptime(d, '%Y-%m-%d'),
              help='Start date of data - format YYYY-MM-DD')
@click.option("--end_date",
              type=lambda d: datetime.strptime(d,
                                               '%Y-%m-%d'),
              help='End date of data - format YYYY-MM-DD')
@click.option("--currency_pair",
              type=click.Choice(CURRENCY_OPTIONS),
              help='Currency paid')
@click.option("--source",
              type=click.Choice(SOURCES),
              help='Source of the data ')
def plot(*args, **kwargs):
    graph = Plot(**kwargs)
    graph.plot()


if __name__ == "__main__":
    plot()
