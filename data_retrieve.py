import datetime
import os
from datetime import date, timedelta
from time import strptime
from urllib.parse import urlencode

import requests as q

today = date.today()
start_date = today - timedelta(days=1)


class QUANDLDATA(object):
    data = []
    currency_pair = "FB"
    source = "WIKI"
    end_date = today.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    url = 'https://www.quandl.com/api/v3/datasets/{0}/{1}/{2}?'
    api_key = os.environ.get("QUANDL_API_KEY")
    return_format = 'data.json'

    def __init__(self, *args, **kwargs):
        if kwargs.pop('currency_pair', None) is not None:
            self.currency_pair = kwargs.get('currency_pair')
        if kwargs.pop('source', None) is not None:
            self.source = kwargs.get('source')

    def date_range(self, start_date, end_date):
        if start_date is not None:
            self.start_date = start_date.strftime("%Y-%m-%d")
        if end_date is not None:
            self.end_date = end_date.strftime("%Y-%m-%d")
        return self.start_date, self.end_date

    def get_data(self, start_date=None, end_date=None,
                 currency_pair=None, source=None, **kwargs):
        """Get sample data

        Args:
            start_date (date, optional): start date 
            end_date (date, optional): end date

        Returns:
            data
        """
        self.currency_pair = currency_pair if currency_pair else self.currency_pair  # noqa
        self.source = source if source else self.source
        start, end = self.date_range(start_date, end_date)

        url = self.url_parse(start_date=self.start_date,
                             end_date=self.end_date, **kwargs)
        
        data = q.get(url, {'API_KEY': self.api_key})
        if data:
            self.data = data.json()
            self.has_been_called = True
            return self.data
        raise Exception(data.json())

    def get_metadata(self):
        assert self.has_been_called == True, "call get data"  # noqa
        meta = self.data.get("dataset_data")
        return meta

    def url_parse(self, **kwargs):
        params = urlencode(kwargs)
        url = self.url.format(
            self.source, self.currency_pair, self.return_format) + params
        return url
