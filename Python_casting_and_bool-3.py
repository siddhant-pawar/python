##################################################
#Types casting variables
##################################################
a = int(5.4)
afloat = str(34)
b = str(1j)
c = b"siddhant"
x = float(5)
y = "siddhant"
z = True

# printing casted variables 
print(type(a))
print(type(b))
print(type(c))
print(type(x))
print(type(y))
print(type(z))

# casting list, sets, tuple.
t= [a,b,c,x,y,z]
print(type(t))

s = set(t)
print(type(s))

tu = tuple(s)
print(type(tu))

################################################
#Booleans
################################################
sint = int(766)
print(bool(sint))
sfloat = float(78)
print(bool(sfloat))
print(sint == sfloat)
print(sint >= sfloat)
print(sint <= sfloat)

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
# Values of list, sets, tuple. are true
print(bool(tu))
print(bool(t))
print(bool(s))


