Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=7
>>> type(a)
<class 'int'>
>>> b=100
>>> type(b)
<class 'int'>
>>> c=8.7
>>> type(c)
<class 'float'>
>>> d="code"
>>> type(d)
<class 'str'>
>>> e="adithya"
>>> type(e)
<class 'str'>
>>> f='''Nagendra'''
>>> type(f)
<class 'str'>
>>> g='p'
>>> type(g)
<class 'str'>
>>> x=5+9j
>>> type(x)
<class 'complex'>
>>> y=3j+8
>>> type(y)
<class 'complex'>
>>> z=7j
>>> type(z)
<class 'complex'>
>>> a=6+3i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> NameError: name 'j' is not defined
SyntaxError: invalid syntax
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
a=true
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a="true"
type(a)
<class 'str'>
