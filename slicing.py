Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:9]
'codegnan'
>>> b="simple is better than complex"
>>> b[0:7]
'simple '
>>> b[11:17]
'etter '
>>> b[10:17]
'better '
>>> b[24:]
'mplex'
>>> b[22:]
'complex'
>>> c="beautiful is better than ugly"
>>> c[0:]
'beautiful is better than ugly'
>>> c[0:9]
'beautiful'
>>> c[13:19]
'better'
>>> c[24:]
' ugly'
>>> #negative slicing
>>> a="word hard until you succeed"
>>> a[-7:]
'succeed'
>>> a[-25:-21]
'rd h'
>>> a[-21:25]
'ard until you succe'
>>> a[-21:-25]
''
>>> b="vijayawada is a royal city"
>>> b[-26:]
'vijayawada is a royal city'
>>> b[-26:-16]
'vijayawada'
>>> b[-10:-5]
'royal'
>>> b[-4:]
'city'
