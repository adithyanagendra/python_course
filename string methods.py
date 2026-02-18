Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
#length #len
#length #len
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#all this files contains string methods only
#find a string
a=
SyntaxError: invalid syntax
a="code"
a.find("t)
       
SyntaxError: unterminated string literal (detected at line 1)
a.find("t")
       
-1
a.find("d")
       
2
a[2]
       
'd'
b="codegnan"
       
b.find("n")
       
5
a[5]+a[7]
       
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[5]+a[7]
IndexError: string index out of range
b[5]+b[7]
       
'nn'
#find string can not find a repeated string
       
#escape sequences
       
#\n->new line
       
#\t->tab space
       
a="name\nmobile\tmailid\ncity"
       
print(a)
       
name
mobile	mailid
city
a="name:adithya nagendra gummaadi\nmobile number=8688712202\nmailid=adithyagummadi4560@gmail.com\tcity=vijayawada"
       
print(a)
       
name:adithya nagendra gummaadi
mobile number=8688712202
mailid=adithyagummadi4560@gmail.com	city=vijayawada
#replace
       
a="wait until you succeed"
       
a.replace("wait","work")
       
'work until you succeed'
b="wait wait until you succeed"
       
b.replace("wait","work")
       
'work work until you succeed'
b.replace("wait","work",1)
       
'work wait until you succeed'
#upper()
       
a="code"
       
a.upper()
       
'CODE'
#lower()
       
b="python"
       
b.lower()
       
'python'
#capitalize
       
c="adithya"
       
c[0].upper()
       
'A'
#this works in indexing
       
#how to convert starting letter into capital
       
c.capitilize()
       
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    c.capitilize()
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?
c.capitalize()
       
'Adithya'
d="python course"
       
d.title()
       
'Python Course'
e="i am in class"
       
e.title()
       
'I Am In Class'
#isupper
       
a="python"
       
a.isupper()
       
False
#islower
       
a.islower()
       
True
#is alpha
       
a.isalpha()
       
True
#is digit
       
a.isdigit()
       
False
b="python course"
       
b.isalpha()
       
False
b.isdigit()
       
False
d=5678
       
d.isdigit()
       
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="5678"
       
d.isdigit()
       
True
e="codegnan"
       
e.startwith("c")
       
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    e.startwith("c")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
e.startswith("c")
       
True
e.endswith("n")
       
True
e.endswith("k")
       
False
#alnum
       
a="adithya"
       
a.isalnum()
       
True
b="adithya2"
       
b.isalnum()
       
True
#strip() it removes the extra spaces
       
a="      adithya   "
       
a.strip()
       
'adithya'
#leftstrip
       
a.lstrip()
       
'adithya   '
a.rstrip()
       
'      adithya'
#split()
       
a="python java c c++"
       
a.split()
       
['python', 'java', 'c', 'c++']
b="i love python"
       
b.split()
       
['i', 'love', 'python']
c="pythonjavacc++"
       
c.split()
       
['pythonjavacc++']
['pythonjavacc++']
       
['pythonjavacc++']

#join()
       
a="python","java","c"
       
"".join(a)
       
'pythonjavac'
" ".join(a)
       
'python java c'
b="python" "java" "c"
       
"".join(b)
       
'pythonjavac'
#concatenation
       
a="code"
       
b="gnan"
       
print(a+b)
       
codegnan
a="python"
       
b="course"
       
print(a+b)
       
pythoncourse
print(a+" "+b)
       
python course
#user test case example
       
fname="adithya"
       
lname="nagendra"
       
print(fname+lname)
       
adithyanagendra
print(fname+" "+lname)
       
adithya nagendra
print(fname.title()+" "+lname.title())
       
Adithya Nagendra
print(fname+" "+lname).title()
       
adithya nagendra
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
       
Adithya Nagendra
#in this we use title at the last of the print statement ,we can use captilize using for every string to get captial,we need to use title to get whole string capital at first
       
#formatting
       
a=4
       
b=5
       
print("the sum of",a+b)
       
the sum of 9
x="adithya"
       
y="nagendra"
       
print("full name is",x+y)
       
full name is adithyanagendra
print("full name is",x+" "+y)
       
full name is adithya nagendra
print(("full name is",x+" "+y).title())
       
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print(("full name is",x+" "+y).title())
AttributeError: 'tuple' object has no attribute 'title'
>>> prijt("full name is",(x+" "+y).title())
...        
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    prijt("full name is",(x+" "+y).title())
NameError: name 'prijt' is not defined. Did you mean: 'print'?
>>> print("full name is",(x+" "+y).title())
...        
full name is Adithya Nagendra
>>> #format method
...        
>>> a="motu"
...        
>>> b="patlu"
...        
>>> print("hello",a+b)
...        
hello motupatlu
>>> print("hello {}{}".format(a,b))
...        
hello motupatlu
>>> print("hello {} {}".format(a,b))
...        
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
...        
hello motu hello patlu
>>> print("hello {} hello {}".format(a,b).title())
...        
Hello Motu Hello Patlu
>>> Hello Motu Hello Patlu
...        
SyntaxError: invalid syntax
>>> #format string
...        
>>> a="john"
...        
>>> b="henry"
...        
>>> print(f"hello {a}{b})")
...        
hello johnhenry)
>>> print(f"hello {a} {b}")
hello john henry
>>> print(f"hello {a} hello {b}".title())
Hello John Hello Henry
