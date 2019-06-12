
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

from data_retrieve import QUANDLDATA


class Plot(object):
    data = []

    def __init__(self, fig):
        self.ax1 = fig.add_subplot(1, 1, 1)

    def __clean_data(self, request):
        data = request.get("dataset_data").get("data")
        headers = request.get("dataset_data").get("column_names")
        headers.extend(data)
        return headers

    def plot(self):
        q = QUANDLDATA()
        data = q.get_data()
        clean_data = self.__clean_data(data)

        self.ax1.clear()
        self.ax1.plot(clean_data[0])
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Live graph with matplotlib')
        return plt
