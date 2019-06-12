import os
from urllib.parse import urlencode

import requests as q


class QUANDLDATA(object):
    currency_pair = "WIKI/FB"
    url = 'https://www.quandl.com/api/v3/datasets/{0}/{1}?'
    api_key = os.environ.get("QUANDL_API_KEY")
    return_format = 'data.json'

    def date_range(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        return self.start_date, self.end_date

    def get_data(self, start_date=None, end_date=None):
        start, end = self.date_range(start_date, end_date)
        url = self.url_parse()
        data = q.get(url, {'API_KEY': self.api_key}).json()
        self.data = data
        self.has_been_called = True
        return data

    def get_metadata(self):
        assert self.has_been_called == True, "call get data"  # noqa
        meta = self.data.get("dataset_data")
        return meta

    def url_parse(self, **kwargs):
        params = urlencode(kwargs)
        url = self.url.format(self.currency_pair, self.return_format) + params
        return url
