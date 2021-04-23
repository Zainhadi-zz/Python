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

CODE = "EFWE WW W @# 12434332"
EMAIL = "john@gmail.com"
PASS1 = "makingpancakes"
PASS2 = "makingtea"

print("TOP SECURE NETWORK")
email = input("Enter email address : ")
password = input("Enter password : ")

if email == EMAIL and password == PASS1:
    print("LEVEL 1 ACCESS GRANTED")
    password1 = input("Enter complete access passcode : ")
    if password1 == PASS2:
        print("TOP CODE IS ",CODE)
    else:
        print("YOUR LOCKED OUT")
else:
    print("ACCESS DENIED")