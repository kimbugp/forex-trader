import pandas as pd
import plotly as plt

from data_retrieve import QUANDLDATA


class Plot(object):
    data = []

    def __clean_data(self, request):
        data = request.get("dataset_data").get("data")
        headers = request.get("dataset_data").get("column_names")
        clean_data = pd.DataFrame(data, None, list(
            map(lambda x: x.lower(), headers)))
        clean_data.date = pd.to_datetime(clean_data.date, format="%Y-%M-%d")
        return clean_data

    def plot(self):
        q = QUANDLDATA()
        data = q.get_data('2015-05-24', '2015-05-28')
        clean_data = self.__clean_data(data)
        trace = go.Ohlc(x=clean_data.date, open=clean_data.open,
                        close=clean_data.close, high=clean_data.high,
                        low=clean_data.low, name="Currencies")
        data = [trace]
        plt.offline.plot(data, filename="text.html")
        return plt
