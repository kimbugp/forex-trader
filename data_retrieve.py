import datetime
import os
from datetime import date, timedelta
from time import strptime
from urllib.parse import urlencode

import requests as q

today = date.today()
start_date = today - timedelta(days=1)


class QUANDLDATA(object):
    currency_pair = "WIKI/FB"
    end_date = today.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    url = 'https://www.quandl.com/api/v3/datasets/{0}/{1}?'
    api_key = os.environ.get("QUANDL_API_KEY")
    return_format = 'data.json'

    def date_range(self, start_date, end_date):
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        return self.start_date, self.end_date

    def get_data(self, start_date=None, end_date=None):
        """Get sample data

        Args:
            start_date (date, optional): start date 
            end_date (date, optional): end date

        Returns:
            data
        """
        start, end = self.date_range(start_date, end_date)
        url = self.url_parse(start_date=self.start_date,
                             end_date=self.end_date)
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
