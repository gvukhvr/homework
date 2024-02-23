#1
from datetime import datetime, timedelta
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print( five_days_ago.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print( yesterday.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print( tomorrow.strftime("%Y-%m-%d"))


#3
from datetime import datetime
current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)
print(without_microseconds)

#4
from datetime import datetime

date1 = datetime(2024, 2, 23, 12, 0, 0)
date2 = datetime(2024, 2, 24, 12, 0, 0)
difference_in_seconds = abs((date2 - date1).total_seconds())
print( difference_in_seconds)