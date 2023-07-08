"""
# Write code to perform operation on:
-List
-Tuples
-Dictionaries
-Sets
"""
import random as rn
####################################################################
#Python - List
####################################################################

a = ["siddhant", "harish", "pratik", "sushil"]
print("Access List Items")
print(a[0]+a[1])

print("Change List Items")
a[2]="roshan"
print(a)

print("Add List Items")
a.append("pratik")
print(a)

print("Remove List Items")
popele = a.pop()
print(popele)
a.append(popele)
a.remove("pratik")
print(a)

print("Loop Lists")
for d in range(len(a)):
    print(a[d])
x=0
while x < len(a):
    print(a[x])
    x = x + 1

print("List Comprehension")
nlist = [y for y in range(100) if y%3 ==0]
print(f"{nlist}")

print("Sort Lists")

sortlist =  []
for s in range(8):
    f = rn.randint(1,23)
    sortlist.append(f)
print(sortlist)
sortlist.sort()
print(sortlist)
sortlist.sort(reverse=True)
print(sortlist)

print("Copy a List")
Copylist =  []
for fd in range(8):
    fd = rn.randint(1,24)
    Copylist.append(fd)
print(Copylist)
Copied = list(Copylist)
print(Copied)
print("append function")
Copyapp = [] 
Copyapp.append(Copied)
print(Copyapp)

print("Join Lists")

Join = ["siddhant", "harish", "pratik", "sushil"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

Joined = []
Joined = Join + fruits
print(Joined)





####################################################################
#Python - Tuples
####################################################################
print("Access Tuple Items")
Access = ("siddhant", "harish", "pratik", "sushil")
print(Access[1])
print(Access[0:-2])
print(Access[1:3])

print("Update Tuples")
Update = ("siddhant", "harish", "pratik", "sushil")
print(dir(Update))
Updatelist = list(Update)
print(dir(Updatelist))
Updatelist[2] = "roshan"
print(Updatelist)
print(a[1:3])

print("Unpack Tuples")
print("Loop Tuples")
print("Join Tuples")



####################################################################
#Python - Dictionaries
####################################################################
g = "Concatenation"
h = "Strings"
print(g+' '+h)
print(g+h)
print(g+'='+h)

####################################################################
#Python - Sets
####################################################################

h = "The Docker {sd} platform allows you to package up your {no} and deliver them to the cloud without any dependencies."
print(h.format(sd="previously called “dot-docker”",no="applicationds"))

