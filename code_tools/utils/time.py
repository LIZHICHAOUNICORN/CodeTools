import datetime
from datetime import timedelta
from tools.utils.logger import logger


# for example: "20220801"
def create_date_fmt0(delta=1, specific_time=None):
    if specific_time is None:
        date_time = datetime.datetime.now() - timedelta(days=delta)
    else:
        date_time = specific_time

    # getting the year from the current date and time
    time_fmt = date_time.strftime("%Y%m%d")
    return time_fmt


# for example: "2022-08-01"
def create_date_fmt1(delta=1, specific_time=None):
    if specific_time is None:
        date_time = datetime.datetime.now() - timedelta(days=delta)
    else:
        date_time = specific_time

    # getting the year from the current date and time
    time_fmt = date_time.strftime("%Y-%m-%d")
    return time_fmt


# for example: "05"
def create_hour_fmt(date_delta=0, hour_delta=0):
    date_time = datetime.datetime.now() - timedelta(days=date_delta,
                                                    hours=hour_delta)
    # getting the year from the current date and time
    time_fmt = date_time.strftime("%H")
    return time_fmt