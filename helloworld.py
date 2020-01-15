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

#
