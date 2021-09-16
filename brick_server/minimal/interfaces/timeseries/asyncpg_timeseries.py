from brick_data.timeseries import AsyncpgTimeseries

from brick_server.minimal.interfaces.timeseries.base_timeseries import BaseTimeseries


class AsyncpgTimeseries(AsyncpgTimeseries, BaseTimeseries):
    def __init__(self, *args, **kwargs):
        super(AsyncpgTimeseries, self).__init__(*args, **kwargs)
