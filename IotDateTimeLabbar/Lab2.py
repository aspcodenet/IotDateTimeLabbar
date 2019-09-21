import datetime

datum = datetime.datetime.now()

print(f"År: {datum.year}")
print(f"Månad: {datum.month}")
print(f"Day: {datum.day}")
print(f"Hour: {datum.hour}")
print(f"Minute: {datum.minute}")
print(f"Second: {datum.second}")
print(f"Millisecond: {datum.microsecond/1000}")
