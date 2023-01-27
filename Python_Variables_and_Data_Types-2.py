#global variables
a = 5.4
b = complex(1j)
c = b"siddhant"
x = 5
y = "siddhant"
z = True
# printing data-types 
print(type(a))
print(type(b))
print(type(c))
print(type(x))
print(type(y))
print(type(z))

# printing data-types of list, sets, tuple.
t= [a,b,c,x,y,z]
print(type(t))

s = set(t)
print(type(s))

tu = tuple(s)
print(type(tu))

for r in t:
    print(type(r))

def globbel():
    #local variable
    t = "sodd"
    print(t)
    print(type(t))
#function call
globbel()
#printing list
print(t)