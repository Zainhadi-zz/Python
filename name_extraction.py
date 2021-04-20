# name = "this is my name zain hadi ansari"

# print("this is my first name",name[16:20])

# #more dynamic

# name = input("Enter your name here :")

# indexspace = name.index(" ")


# print("this is your first name",name[:indexspace])
# print("this is your last name",name[indexspace:])


# email = input("Enter your email address")


# name = email[:email.index("@")]
# second = email[email.index("@"):email.rindex(".")]
# last = email[email.rindex(".")+1:]
# print(name,second,last,sep="\n")

email = input("Enter your email address : ")

indexusername = email.index("@")
indexdomain = email.rindex(".")

name = email[:indexusername]
second = email[indexusername+1:indexdomain]
last = email[indexdomain+1:]

print(name,second,last,sep="\n")