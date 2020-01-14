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


