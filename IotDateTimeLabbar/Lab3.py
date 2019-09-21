import datetime

def ToSwedishName(weekdayNum):
    if(weekdayNum == 0):
        return "Måndag"
    if(weekdayNum == 1):
        return "Tisdag"
    if(weekdayNum == 2):
        return "Onsdag"
    if(weekdayNum == 3):
        return "Torsdag"
    if(weekdayNum == 4):
        return "Fredag"
    if(weekdayNum == 5):
        return "Lördag"
    if(weekdayNum == 6):
        return "Söndag"


datum = datetime.datetime.now()
weekday = datum.weekday()

print(f"Veckodag: {weekday}")

import calendar
print(calendar.day_name[weekday])

print(f"Veckodag: {ToSwedishName(weekday,False)}")
