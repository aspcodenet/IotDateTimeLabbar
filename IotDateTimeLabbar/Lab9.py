import datetime

day = int(input("Ange dag"))
month = int(input("Ange månadsnummer"))
year = int(input("Ange år"))

datum1 = datetime.datetime.now()
datum2 = datetime.datetime(year,month,day)

if datum1.date() == datum2.date():
    print("Samma")
