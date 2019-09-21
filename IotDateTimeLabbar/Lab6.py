import datetime


datumString = input("Ange datum")
datum = datetime.datetime.strptime( datumString, "%Y-%m-%d")

print(datum)

