#CRUD
# C = Create
# R = Read
# U = Update
# D = Delete

# write mode

# file_object = open("code_1.txt","w")

# file_object.write("This is a file write operation! overide")


# file_object.close()

# read mode

data_3 = []

file_object = open("dataset.csv","r")

data = file_object.readline()

# print(data)

data_1 = file_object.readlines()

# print(data_1)

for each in data_1:
    name,salary = each.split(",")
    if "\n" in salary:
        salary = salary[:-2]
    salary = int(salary)
    data_3.append((name,salary))
    print("Name : {} and Salary : {}".format(name,salary))
data_3.sort(key = lambda a: a[1])
print(data_3)








