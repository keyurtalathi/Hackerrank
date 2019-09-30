from datetime import datetime


def datetime_to_utcms(date_time, months_delta=1, days_delta=1):
    date = int(date_time.strftime("%s")) * 1000
    delta = int(
        datetime(year=1970, month=months_delta, day=days_delta).strftime("%s")) * 1000
    date = date + delta
    return date


def get_datetime_from_utcms(epoch):
    date_time = datetime.fromtimestamp(epoch / 1000)
    return datetime