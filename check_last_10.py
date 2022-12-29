from datetime import datetime, timedelta
import pytz
def check_last_10(most_recent_notification):
    utc=pytz.UTC
    most_recent_time = most_recent_notification[2]
    time_now = utc.localize(datetime.utcnow())
    return most_recent_time > time_now - timedelta(minutes=10)