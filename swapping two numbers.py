Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #swapping of two varaibles
>>> a=10
>>> a,b=b,a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b=b,a
NameError: name 'b' is not defined
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print("the a value is ",a)
the a value is  20
>>> print("the value is",b)
the value is 10
>>> #method1
>>> #method2
>>> a=10
>>> b=20
>>> temp=a
>>> a=b
>>> b=temp
>>> print("the a value is ",a)
the a value is  20
>>> print("the a value is ",b)
the a value is  10
>>> #method3
>>> a=10
>>> b=20
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print("the a value is ",a)
the a value is  20
>>> print("the a value is ",b)
the a value is  10
>>> #method4
>>> a=10
>>> b=20
>>> a=a+b
>>> b=a-b
>>> a=b-a
>>> print("after swapping a=%d,b=%d" %(a,b))
after swapping a=-20,b=10
