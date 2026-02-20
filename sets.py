Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,5.6,"pooja",5+9j,True,False}
print(a)
{False, True, (5+9j), 'pooja', 3, 5.6}
type(a)
<class 'set'>
b={7,9,5,6,7,9,3}
print(b)
{3, 5, 6, 7, 9}
type(b)
<class 'set'>
a={4,5,6,7,8,9}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 20}
#issubset()
a={2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False
a={123456}
b={7,8,9,10}
a.issubset(b)
False
b.issubset(a)
False
#superset
a={3,4,5,6,7,8}
b={2,3,4,5}
a.issuperset(b)
False
b.issuperset(a)
False
a={1,2,3,4,5,6}
b={3,4,5}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={3,4,5,6,7,8}
b={2,3,4,5,6}
a.union(b)
{2, 3, 4, 5, 6, 7, 8}
b.union(a)
{2, 3, 4, 5, 6, 7, 8}
#intersection
a={4,5,6,7,8,9}
b={2,3,4,5,6}
a.intersection(b)
{4, 5, 6}
b.intersection(a)
{4, 5, 6}
#difference
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}
b.difference(a)
{8, 7}
#update
a={9,10,11,12,13}
b={11,12,13,14}
a.update(b)
a
{9, 10, 11, 12, 13, 14}
b.update(a)
b
{9, 10, 11, 12, 13, 14}
#difference update
#after updating previous set will not be recognized and we need to take latest set as the fuction
a={123456}
b={7,8,9,10,11,12}
a.diffrenceupdate(b)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.diffrenceupdate(b)
AttributeError: 'set' object has no attribute 'diffrenceupdate'. Did you mean: 'difference_update'?
a.difference_update(b)
a
{123456}
a={2,3,4,5,6,7}
b={1,5,7,9,11,12}
a.difference_update(b)
a
{2, 3, 4, 6}
b.difference_update(a)
b
{1, 5, 7, 9, 11, 12}
a={1,2,3,4,5,6}
b={7,8,9,10,11,12}
a.difference_update(b)
a
{1, 2, 3, 4, 5, 6}
#symmetric difference
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}
a
{3, 4, 5, 6, 7, 8, 9}
b
{1, 2, 3, 8, 9, 10, 11}
#note only on the function of update it will update the values otherwise it does not
#symmetric_difference_update()
a={1,3,5,7,9,11,13}
b={2,4,6,8,10,12}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b
{1, 3, 5, 7, 9, 11, 13}
#intersection_update
a={7,8,9,10,11,12,13}
b={2,3,4,5,6,7,8,9}
a.intersection_update(b)
a
{8, 9, 7}
a
{8, 9, 7}
b.intersection_update(a)
b
{8, 9, 7}
b
{8, 9, 7}
#pop and remove
a={5,6,7,8,9,10}
a.pop()
5
a.remove(10)
a
{6, 7, 8, 9}
#copy,clear,add
a={3,4,5,6,7}
a.clear()
a
set()
a={3,4,5,6,7}
a.copy()
{3, 4, 5, 6, 7}
b=set()
b.add(60)
b
{60}
#discard
b.discard(60)
b
set()
>>> #isdisjoint
>>> a={3,4,5,6,7,8}
>>> b={2,3,4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a=[7,8,9]
>>> b=[2,3,4]
>>> a.isdisjoint(b)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.isdisjoint(b)
AttributeError: 'list' object has no attribute 'isdisjoint'
>>> a.isdisjoint(b)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.isdisjoint(b)
AttributeError: 'list' object has no attribute 'isdisjoint'
>>> a={7,8,9}
>>> b={2,3,4}
>>> a.isdisjoint(b)
True
>>> #count ,index and len
>>> a={5,6,7,8}
>>> len()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> len(a)
4
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
