Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"adithya","year":2026,"month":2}
print(a)
{'name': 'adithya', 'year': 2026, 'month': 2}
type(a)
<class 'dict'>
b={"name","year","month"}
print(b)
{'month', 'year', 'name'}
type(b)
<class 'set'>
a={"name":"pooja","year":2006,"month":2}
a.keys()
dict_keys(['name', 'year', 'month'])
#keys
#values
a.values()
dict_values(['pooja', 2006, 2])
#items
a.items()
dict_items([('name', 'pooja'), ('year', 2006), ('month', 2)])
b=("name":)
SyntaxError: invalid syntax
b={"name":}
SyntaxError: expression expected after dictionary key and ':'
#accessing
a={"name":"Adithya","year":2026}
a["year"]
2026
a[2026]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[2026]
KeyError: 2026
#update
a={"name":"adithya","city":"vja"}
a.update({"mailid":adithyagummadi4560@gmail.com})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.update({"mailid":adithyagummadi4560@gmail.com})
NameError: name 'adithyagummadi4560' is not defined
>>> a.update({"mailid":"adithyagummadi4560@gmail.com"})
>>> a
{'name': 'adithya', 'city': 'vja', 'mailid': 'adithyagummadi4560@gmail.com'}
>>> a.update({"date":20},{"month":4})
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.update({"date":20},{"month":4})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"date":20,"month":4})
>>> a
{'name': 'adithya', 'city': 'vja', 'mailid': 'adithyagummadi4560@gmail.com', 'date': 20, 'month': 4}
>>> #setdefault
>>> a={"name":"adithya","hour":01,"sec":2)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a={"name":"adithya","hour":1,"sec":2)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={"name":"adithya","hour":01,"sec":2}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> a={"name":"adithya","hour":1,"sec":2}
>>> a.setdefault("date",20)
20
>>> a.setdefault(20,"date")
'date'
>>> #here fisrt will be taken as key
>>> #pop
>>> a={"colour":"black","food":"biriyani"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("colour")
'black'
>>> a
{'food': 'biriyani'}
>>> a
{'food': 'biriyani'}
>>> #pop item
>>> a={"name":"adithya","age":20,"year":2026}
>>> a.popitem()
('year', 2026)
>>> a
{'name': 'adithya', 'age': 20}
