#Write Sin Strings with ''' or """ quotes.
a = "The Docker (previously called “dot-docker”) platform allows you to package up your application(s) and deliver them to the cloud without any dependencies."
print(a)

#Write Multiline Strings with ''' or """ quotes.
b = """The Docker (previously called “dot-docker”) platform allows you to package up your application(s) and deliver them to the cloud without any dependencies.
If you have begun creating cloud-based applications, you should get a strong understanding of the benefits of Docker. 
This platform is a great way to create isolated environments and automatically scale them up or down."""
# printing Multiline Strings
print(b)

# printing particular char
c = "hello, world!!"
print(c[3])
# printing particular set of char
print(c[7:12])

#Looping Through a String
for f in "hello, Python!!":
     print(f)

#Printing String Length
for f in range(len(c)):
    print(c[f])

print(len(c))

#To check if any certain phrase or character is present in a string
print("package" in b)
print("package" not in b)

####################################################################
#Python - Modify Strings
####################################################################

e = a
print(e.replace("d","p"))
print(e.upper())
print(e.lower())
print(e.capitalize())
elist = e.split(",")
print(elist)


####################################################################
#Python - Slicing Strings
####################################################################
f = "Slicing Strings"
print(f)
print(f[:7])
print(f[:-4])
print(f[-1:-4])
print(f[1:4])

####################################################################
#Python - Concatenation Strings
####################################################################
g = "Concatenation"
h = "Strings"
print(g+' '+h)
print(g+h)
print(g+'='+h)

####################################################################
#Python - Format Strings
####################################################################

h = "The Docker {sd} platform allows you to package up your {no} and deliver them to the cloud without any dependencies."
print(h.format(sd="previously called “dot-docker”",no="applicationds"))

####################################################################
#Python - Escape Characters Strings
####################################################################

txt = "The Docker platform allows you to package up your application(s) \n deliver them to the cloud\' without any dependencies."
print(txt)
