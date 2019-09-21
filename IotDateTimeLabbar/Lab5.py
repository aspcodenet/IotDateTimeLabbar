import datetime
import calendar



datum = datetime.datetime.now()
for i in range(0,9):
    print(datum.strftime("%Y-%m-%d"))
    datum = datum + datetime.timedelta(days=40)

