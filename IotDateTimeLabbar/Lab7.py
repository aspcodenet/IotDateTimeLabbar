

import datetime

year = int(input("Ange år"))
month = int(input("Ange månad"))
datum = datetime.datetime(year,month,1)
datumNextMonth = datum  + datetime.timedelta(days=31)
datumFirstNextMonth = datetime.datetime(datumNextMonth.year,datumNextMonth.month,1)
lastThisMonth = datumFirstNextMonth + datetime.timedelta(days=-1)


print(lastThisMonth.day)


