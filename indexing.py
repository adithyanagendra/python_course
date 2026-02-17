Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
#positive indexing
a="vijayawada"
a[0]
'v'
a[1]
'i'
a[2]
'j'
a[3]
'a'
a[4]
'y'
a[5]
'a'
a[6]
'w'
a[7]
'a'
a[8]
'd'
a[9]
'a'
b="i am in class"
b[0]
'i'
b[2]+b[3]
'am'
b[5]+b[6]
'in'
b[8]+b[9]+b[10]+b[11]
'clas'
b[8]+b[9]+b[10]+b[11]+b[12]
'class'
c="i love python"
c=[2]+[3]+[4]+[5]
c[2]+c[3]+c[4]+c[5]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c[2]+c[3]+c[4]+c[5]
IndexError: list index out of range
>>> c[2]+c[3]+c[4]+c[5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c[2]+c[3]+c[4]+c[5]
IndexError: list index out of range
>>> del(c)
>>> c="i love python"
>>> c[1]
' '
>>> c[2]+c[3]+c[4]+c[5]
'love'
>>> c[7]+c[8]+c[9]+c[10]+c[11]+c[12]
'python'
>>> d="time is precious"
>>> d[0]+d[1]+d[2]+d[3]+d[4]
'time '
>>> d[6]+d[7]
's '
>>> d[6]+d[7]
's '
>>> d[9]+d[10]+d[11]+d[12]+d[13]+d[14]+d[15]+d[16]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d[9]+d[10]+d[11]+d[12]+d[13]+d[14]+d[15]+d[16]
IndexError: string index out of range
>>> d[6]+d[7]
's '
>>> d[9]+d[10]
're'
>>> d[8]+d[9]+d[10]
'pre'
>>> KeyboardInterrupt
>>> d[8]+d[9]+d[10]+d[11]+d[12]+d[13]+d[14]+d[15]
'precious'
>>> #negative indexing
>>> a="word hard"
>>> a[-9]+a[-8]+a[-7]+a[-6]
'word'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'hard'
>>> b="i am learning python"
>>> b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
>>> b[-15]+b[-14]+b[-13]+b[-12]+b[-11]+b[-10]+b[-9]+b[-8]
'learning'
