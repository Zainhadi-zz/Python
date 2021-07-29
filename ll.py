import sys

# z = int(input("enter the number"))

# if z%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# a = int(input())
# b = int(input())

# if (a+b<10) and a>0:
#     print("we are good")

# else:
#     print("we are in trouble")

# s = input("Enter the string: ")

# if s == s[::-1]:
#     print(s,"it is palindrome")
# else:
#     print(s,"is not palindrom")

#nested if else

# CODE = "EFWE WW W @# 12434332"
# EMAIL = "john@gmail.com"
# PASS1 = "makingpancakes"
# PASS2 = "makingtea"

# print("TOP SECURE NETWORK")
# email = input("Enter email address : ")
# password = input("Enter password : ")

# if email == EMAIL and password == PASS1:
#     print("LEVEL 1 ACCESS GRANTED")
#     password1 = input("Enter complete access passcode : ")
#     if password1 == PASS2:
#         print("TOP CODE IS ",CODE)
#     else:
#         print("YOUR LOCKED OUT")
# else:
#     print("ACCESS DENIED")

# a = int(input("Enter value to check"))

# if a%5 == 0 and  a%3 == 0:
#     print("Fuzz Buzz")
# elif a%5 == 0:
#     print("Fuzz")
# elif a%3 == 0:
#     print("Buzz")
# else:
#     print("Nothing in return")

e = input("Enter email : ")

"""
there should be one @
there should be . after @
there be atleast 2 character between @ and .
there should be atleast 2 character after the dot
"""
hatr = e.find("@") > -1
if not hatr:
    print("There is not @")
    sys.exit()
else:
    hsc = len(e[:e.find("@")]) >2
    hd = e.find(".") -1
    l1 = len(e[e.find("@")+1:e.find(".")]) >2
    l2 = len(e[e.rfind(".")+1:]) >2

    if hatr and hsc and hd and l1 and l2:
        print("Email  is valid")
    else:
        print("Not Valid")