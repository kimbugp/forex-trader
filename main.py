import sys

from argparser import args
from data_plotter import Plot

if __name__ == "__main__":
    graph = Plot(**vars(args))
    graph.plot()
