import pandas as pd

import plotly as plt
import plotly.graph_objs as go
from data_retrieve import QUANDLDATA
from plotly import tools


class Plot(object):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def __clean_data(self, request):
        data = request.get("dataset_data").get("data")
        headers = request.get("dataset_data").get("column_names")
        clean_data = pd.DataFrame(data, None, list(
            map(lambda x: x.lower(), headers)))
        clean_data.date = pd.to_datetime(clean_data.date, format="%Y-%M-%d")
        clean_data.set_index(clean_data.date, inplace=True)
        return clean_data

    def plot(self):
        q = QUANDLDATA()
        self.data = q.get_data(**self.__dict__, collapse='daily')
        clean_data = self.__clean_data(self.data)
        ma = clean_data.close.rolling(center=False, window=30).mean()

        trace = go.Ohlc(x=clean_data.date, open=clean_data.open,
                        close=clean_data.close, high=clean_data.high,
                        low=clean_data.low, name="Currencies")
        trace1 = go.Scatter(x=clean_data.index, y=ma, name="Moving average")
        trace2 = go.Bar(x=clean_data.index, y=clean_data.volume, name="Volume")

        data = [trace, trace1, trace2]

        fig = tools.make_subplots(rows=2, cols=1, shared_xaxes=True)
        fig.append_trace(trace, 1, 1)
        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 2, 1)
        plt.offline.plot(fig, filename="text.html")
        return plt
