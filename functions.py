#functions:1)a function is a block organized,reusable code and that is used to perform a single or multiple tasks.
#2) python gives in build functions like prints, u can make your own function also and this are called user defined functions.
#3)function blocks begin with the keyword def followed by the function name parantheisis(()).
 #difference between normal and functions
'''a=10
b=20
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is ",a*b)
a=100
b=200
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is ",a*b)
a=1000
b=2000
print("the sum is ",a+b)
print("the diff is ",a-b)
print("the product is ",a*b)'''
#functions
'''def calculate(a,b):
    print("the sum is ",a+b)
    print("the diff is ",a-b)
    print("the product is ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''
'''def calculate(a,b):
    print("the power is",a**b)
    print("the rem is",a%b)
    print("the division",a//b)
calculate(10,20)'''

'''def add(a,b):
    print(a+b)
add(5,6)'''
'''def add():
    a=int(input("enter the value of a"))
    b= int(input("enter the value of b"))
    print(a+b)
add()'''
'''def fullname():
    fname=input(



#difference between print and return: print just shows the human user output in a console  return: it is used to terminate a function and gives back a value from the functions'''
'''#print vs return
def mul(a,b):
    print(a*b)
mul(3,4)'''
'''def mul(a,b):
    return a*b
print(mul(2,3))'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b0
    print(c)
    print(d)
    print(e)
cal(3,4)'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c,d,e)
cal(3,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(cal(2,4))'''
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return(c,d,e)
print(cal(2,4))'''

#tasks
'''def calc():
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    option=int(input("enter the option"))
    if option==1:
        return a+b
    if option==2:
        return a-b
    if option==3:
        return a*b
print(calc())'''
'''def calc():
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    option=int(input("enter the option"))
    if option==1:
        print(a+b)
    if option==2:
        print(a-b)
    if option==3:
        print(a*b)
(calc())'''
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    option=int(input("enter the option 1)add 2)sub 3)mul"))
    if option==1:
        add()
    if option==2:
        sub()
    if option==3:
        mul()'''


