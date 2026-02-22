Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list it should be given in square bracket only
#list is mutable means we can change.
a=[3,4.5,"python",6+7j,True,False]
print(a)
[3, 4.5, 'python', (6+7j), True, False]
type(a)
<class 'list'>
b=6
type(b)
<class 'int'>
b=[6]
type(b)
<class 'list'>
#append
a=["python","java","c"]
a.append("c+++")
a
['python', 'java', 'c', 'c+++']
#we can't add two value in the append function
a.append("sql","ml")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("sql","ml")
TypeError: list.append() takes exactly one argument (2 given)
a.append("sql,ml")
a
['python', 'java', 'c', 'c+++', 'sql,ml']
a.append(["sql,ml"])
a
['python', 'java', 'c', 'c+++', 'sql,ml', ['sql,ml']]
# we can only assign only one value are u can assign in one list
c=["python","java","c"]
c.append("html","css")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
c.append(["html","css"])
c
['python', 'java', 'c', ['html', 'css']]
c.extend(["html","css"])
c
['python', 'java', 'c', ['html', 'css'], 'html', 'css']
#insert
a=["apple","banana","mango"]
a.insert(1,"kiwi")
a
['apple', 'kiwi', 'banana', 'mango']
a.insert("berry",3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.insert("berry",3)
TypeError: 'str' object cannot be interpreted as an integer
#we cant no give the string without giving the position
#index
a=["black","blue","red","white"]
a.index("white")
3
a.copy()
['black', 'blue', 'red', 'white']
b=a.copy()
b
['black', 'blue', 'red', 'white']
a
['black', 'blue', 'red', 'white']
#copy
#sort
a=["briyani","ice cream","chocolates"]
a.sort()
a
['briyani', 'chocolates', 'ice cream']
b=[8,6,4,0,2,5]
b.sort()
b
[0, 2, 4, 5, 6, 8]
a=[7,9,"hello","python","animal",4,2,0]
a.sort()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
b=[-8,-7,-5,-1,-2,0]
b.sort()
b
[-8, -7, -5, -2, -1, 0]
#reverse
a=["ml","ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds', 'ml']
b=[7,8,9,4,5,6]
b.reverse()
b
[6, 5, 4, 9, 8, 7]
#pop
#it does not consider string
#either we need to give empty are index
a=["html","cs","js"]
a.pop()
'js'
a
['html', 'cs']
a.pop("cs")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.pop("cs")
TypeError: 'str' object cannot be interpreted as an integer
a.pop("1")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a.pop("1")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'cs'
>>> a
['html']
>>> #remove
>>> a=["hi","hello","how"]
>>> a.remove("hi")
>>> a
['hello', 'how']
>>> #remove method is used to remove a variable in remove method we can remove by passing string.
>>> #length
>>> a="code"
>>> len(a)
4
>>> b=["code"]
>>> b
['code']
>>> len(b)
1
>>> #if we take the input in str formate len is number of characters if we take in list it will take is a whole character in word as 1
>>> #count
>>> a=["sun","star","moon","sky"]
>>> a.count("star")
1
>>> a=["sun","star","moon","sky","sky"]
>>> a.count("sky")
2
>>> b=["hello"]
>>> b.count("1")
0
>>> c=str(a)
>>> c
"['sun', 'star', 'moon', 'sky', 'sky']"
>>> c=str(b)
>>> c
"['hello']"
>>> type(c)
<class 'str'>
>>> c,count("1")
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    c,count("1")
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> c.count("1")
0
>>> c.count("l")
2
#clear
a=["water","drink"]
a.clear()
a
[]
b=[]
type(b)
<class 'list'>
b.append("juice")
b
['juice']
a=[]
type(a)
<class 'list'>
