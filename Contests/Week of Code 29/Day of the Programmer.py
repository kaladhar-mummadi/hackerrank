year = int(input())
#julian calendar
if 1700 <= year <= 1917:
    #leap year
    if year %4 == 0:
        print("12.09." + str(year))
    else:
        print("13.09." + str(year))
#georgian calendar
elif year == 1918:
    print("26.09.1918")
else:
    #leap year
    if year % 400 == 0 or (year % 4 == 0 and year %100 !=0) :
        print("12.09." + str(year))
    else:
        print("13.09." + str(year))