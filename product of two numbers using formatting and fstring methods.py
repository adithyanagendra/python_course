Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #mutiply a*b using formating and f string ,method and normal method
>>> a=4
>>> b=5
>>> print(a*b)
20
>>> #formating method without using another variable
>>> print("the product is {}".format(c))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("the product is {}".format(c))
NameError: name 'c' is not defined
>>> c=a*b
>>> print("the product is {}".format(c))
the product is 20
>>> print(f"the product is {c}")
the product is 20
>>> #upper method is using another variable
>>> #now without variable
>>> print("the product is {}".format(a*b))
the product is 20
>>> print(f"the product is {a*b}")
the product is 20
