year = int(input("Input a year: "))
if year in range(1800,2026):
    if (year % 400 == 0):
        leap_year = True
    elif (year % 100 == 0):
        leap_year = False
    elif (year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
else:
    print("Invalid Input")
    a=input("Press any key to exit")
    quit()

month = int(input("Input a month [1-12]: "))
if month in range (1,13):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
else:
    print("Invalid Input")
    a=input("Press any key to exit")
    quit()


day = int(input("Input a day [1-31]: "))
if day in range(1,32):
    if day <month_length:
        day += 1
    else:
        print("Invalid input")
        b=input("Press any key to exit")
        quit()
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
else:
    print("Invalid Input")
    a=input("Press any key to exit")
    quit()
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))