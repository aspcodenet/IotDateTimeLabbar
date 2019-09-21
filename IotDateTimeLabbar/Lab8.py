
import datetime

datum1 = datetime.datetime.now()
datum2 = datetime.datetime(datum1.year,12,24)
diff = datum2 - datum1

print(diff.days)
