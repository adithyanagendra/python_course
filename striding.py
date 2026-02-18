Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
#rules
#in positive striding high to low is not possible
#in negative striding low to high is not possible
# numbering should be stared by position element indexing number only.
# this is applicable for both positive and negative indexing also.
#examples on positive striding and slicing.
a="cloud computing"
a[::1]
'cloud computing'
a[::3]
'cucpi'
b="data science"
a[::4]
'cdmi'
a[::2]
'codcmuig'
b[::4]
'd e'
>>> b[::2]
'dt cec'
>>> b[::5]
'dsc'
>>> b[::8]
'de'
>>> #slicing
>>> b[1:8]
'ata sci'
>>> b[5:]
'science'
>>> b[3:9]
'a scie'
>>> a[4:10]
'd comp'
>>> a="python course"
>>> a[0:5:2]
'pto'
>>> a[1:8:3]
'yoc'
>>> a[2:12:3]
'tnos'
>>> a[5:12:4]
'nu'
>>> a[1:11:5]
'y '
>>> a[0:9:2]
'pto o'
>>> #negative striding
>>> a="machine learning"
>>> a[-1:-8:-2]
'gire'
>>> a[-1:-12:-4]
'gr '
>>> a[-2:-16:-5]
'nei'
>>> a[-4:-15:-2]
'naleic'
