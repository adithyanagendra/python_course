Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int
int(7)
7
int(7.5)
7
int("Adithya")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("Adithya")
ValueError: invalid literal for int() with base 10: 'Adithya'
int(7+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(false)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
#float
float(8)
8.0
float(8.5)
8.5
float(6+5j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(6+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float("Adithya")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("Adithya")
ValueError: could not convert string to float: 'Adithya'
float(true)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
float(false)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
#str
str(4)
'4'
str(4.5)
'4.5'
str("Adithya")
'Adithya'
str(8+9j)
'(8+9j)'
str(true)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
str(false)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
str("true")
'true'
str("false")
'false'
str(True)
'True'
>>> str(False)
'False'
>>> float(True)
1.0
>>> float(false)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> float(False)
0.0
>>> #complex
>>> complex(9)
(9+0j)
>>> complex(9.8)
(9.8+0j)
>>> complex("adithya")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex("adithya")
ValueError: complex() arg is a malformed string
>>> complex(adithya)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(adithya)
NameError: name 'adithya' is not defined
>>> complex(9+6j)
(9+6j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(9)
True
>>> bool(9.5)
True
>>> bool("adithya")
True
>>> bool(9+6j)
True
>>> bool(True)
True
>>> bool(False)
False
