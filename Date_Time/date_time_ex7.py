# adding days to a date using timedata

from datetime import date,timedelta
today = date.today()
nextweek = today + timedelta(days = 7 )
print(nextweek)

