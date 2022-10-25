import calendar
from calendar import month

year = int(input("insert year : "))
mon = int(input("insert month : "))

print(month(year, mon))
print(calendar.month(year, mon))
