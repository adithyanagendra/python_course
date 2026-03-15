#Global and local varaibles:a variable inside and outside the function is called global and local variables..
#a variable definte above the function and accessible to the entire global space is called a global variable.
#a variable which is inside the function is called local varaibles.


#first case of global variables

'''a=3
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''


#second case of global variables
'''a=2
def check1():
    print("inside values is",a)
check1()
print("outside value is",a)'''

#third case of global varaibles

'''a=4
b=3
def check2():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12 #local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)'''

#fourth case of global varaibles

#usage of global keyword:when user want to access the global varaible  inside the function directly and carry forward the updated value even outside the function the we need to use global keyword.
'''a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''








