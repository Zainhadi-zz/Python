# list vs array 
# list is heterogeneous
# array is homogeneous
import copy
data = [1,2,45,35,5,46,464,42,1,31,31,313]

data1 = ["qwrfw","3wfwfw","3fwfw"]

#print(data,"\n",data1)

#print(data1[-1])


#print(data[:5])

# list1 = [23,43,[2423,24434,[242324,4,34,34,[34,24,24,24,[24,4234]]]]]

# print(list1[2][2][4][4][1])



#list2 = [1,2,3,4,5,6,7,8,9,10]

#print(list2[::2])
#reserve order
#print(list2[::-1])

#mutable

list3 = [3,43,4,43,232,2]

# list3[2]=234

#print(list3)

# list3.append(23)

#print(list3)

# list3.pop()

#print(list3)

# list3.insert(3,999)
# list3.remove(999)
#
#print(list3)

# slicing and list method for copying data
list4 = list(list3)
list4 = list4[:]

print(list4)

list3.pop()

print(list4)
print(list3)

#shallow copy and deep copy

dom = [1,2,3,[2,3,4]]

# dom1 = dom[:]

# dom1[3].append(999)

# print(dom)

# dom1 = copy.copy(dom)
dom1 = copy.deepcopy(dom)

dom1[3].append(900)

print(dom)
print(dom1)


 