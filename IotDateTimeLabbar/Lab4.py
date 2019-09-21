import datetime
import calendar


datum = datetime.datetime.now()

enddate = datum + datetime.timedelta(days=40)

weekday = enddate.weekday()
print(enddate)
print(calendar.day_name[weekday])


