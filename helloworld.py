#Python Tutorial taken from https://www.w3schools.com/python
msg = 'Hello World'
print (msg)

#test comment

x = 5
y = 'John'
print(x,y)

x = 'Python is '
y = 'awesome'
z = x + y
print(z)

#global variables
a = 'awesome!'
def myfunc():
    print('Python is', a)

myfunc()    

#local variables can have the same name is global variables (and not affect the global variable)
#variables created outside functions are global, those created inside functions are local variable

def mylocalfunc():
    a = 'fantastic!!'
    print(x,a)

mylocalfunc()

print(x,a)

#variables created inside the function can be made global by the global function

def myglobalfunc():
    global a
    a = 'globally awesome!'

myglobalfunc()

print(x,a)

#getting the data type

print (type(x))

#Python will auto detec type of variables and numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#Conveting numbers to other types, although complex numbers can't be converted
x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 

#No inbuilt random function but there is a module

import random

print(random.randrange(1,10)) 

#Although Python auto detects variables you can force select

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 

print(x)
print(y)
print(z)

#Multiline strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 