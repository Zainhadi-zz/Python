 # DataValidation
d = input("Enter your birthday : ")
day = int(d[:2])
month = int(d[3:5])
year = int(d[6:])

ivy = year > 1900 and year < 2021
ivm = month >=1 and month <=12
ivdf = day >= 1 and day <=29
ivd = day >= 1 and day <=31
if ivy and ivm:
    if month == 2 and ivdf:
        print("Valid  Date")
    elif month != 2 and ivd:
        print("Valid Date")
    else:
        print("Not Valid Date")
else:
    print("Not Valid data")
