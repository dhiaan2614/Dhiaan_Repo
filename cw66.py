import calendar

year=int(input("Enter Year: "))
month=int(input('Enter Month'))

print("\nMONTH CALENDAR")
print(calendar.month(year,month))\

print("YEAR CALENDAR")
print(calendar.calendar(year))

if calendar.isleap(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")