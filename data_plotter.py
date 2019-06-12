
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_finance import candlestick_ochl

from data_retrieve import QUANDLDATA


class Plot(object):
    data = []

    def __init__(self, fig):
        self.ax1 = fig.add_subplot(1, 1, 1)

    def __clean_data(self, request):
        data = request.get("dataset_data").get("data")
        headers = request.get("dataset_data").get("column_names")
        clean_data = pd.DataFrame(data, None, list(
            map(lambda x: x.lower(), headers)))
        clean_data.date = pd.to_datetime(clean_data.date, format="%Y-%M-%d")
        clean_data.date = pd.to_numeric(clean_data.date)
        return clean_data

    def plot(self):
        q = QUANDLDATA()
        data = q.get_data()
        clean_data = self.__clean_data(data)
        candlestick_ochl(self.ax1, clean_data.values,
                         width=0.4,
                         colorup='#77d879', colordown='#db3f3f')
        self.ax1.clear()
        self.ax1.plot(clean_data)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Live graph with matplotlib')
        return plt
