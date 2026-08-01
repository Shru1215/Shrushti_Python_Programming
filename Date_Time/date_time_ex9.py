from datetime import datetime,date,timedelta

now = datetime.now()
print(now + timedelta(weeks = 1))
print(now + timedelta(hours = 5,minutes = 30))
print(now + timedelta(days = 5, hours = 2, seconds =30))
print(timedelta(minutes = 90))


