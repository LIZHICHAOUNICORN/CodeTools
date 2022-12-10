from cronjob.utils.time import create_date_fmt0
from cronjob.utils.logger import logger
import datetime


def test_date_fmt():
    format_datetime = datetime.datetime(2022, 8, 15, 3, 22, 30, 8)
    date_time = create_date_fmt0(0, format_datetime)
    assert date_time == "20220815"
