Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict part 2
#get
a={"name":"adithya","city":"vij","mail":"a@gmail.com"}
a.get("name")
'adithya'
#copy
a.copy()
{'name': 'adithya', 'city': 'vij', 'mail': 'a@gmail.com'}
#clear
a
{'name': 'adithya', 'city': 'vij', 'mail': 'a@gmail.com'}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b={"mobile no"=8688712202}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> b.update{"mobile no":8688712202}
SyntaxError: invalid syntax
>>> b.update("mobile no":8688712202)
SyntaxError: invalid syntax
>>> a={"name:"adithya","year":2026,"name":"nagendra"}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"name":"adithya","year":2026,"name":"nagendra"}
...    
>>> print(a)
...    
{'name': 'nagendra', 'year': 2026}
>>> ={"name:"adithya","year":2026,"name1":"nagendra"}
...   
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"name":"adithya","year":2026,"name1":"nagendra"}
...   
>>> print(a)
...   
{'name': 'adithya', 'year': 2026, 'name1': 'nagendra'}
>>> a={"idnos"=[10,20,30],"names":["adithya","nagendra","Gummadi"],"places":["vja","hyd","vzg"]}
...   
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a=["idnos"=[10,20,30],"names":["adithya","nagendra","Gummadi"],"places":["vja","hyd","vzg"]]
...   
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a={"idnos":[10,20,30],"names":["adithya","nagendra","Gummadi"],"places":["vja","hyd","vzg"]}
...   
>>> print(a)
...   
{'idnos': [10, 20, 30], 'names': ['adithya', 'nagendra', 'Gummadi'], 'places': ['vja', 'hyd', 'vzg']}
>>> a.keys()
...   
dict_keys(['idnos', 'names', 'places'])
>>> a.items()
...   
dict_items([('idnos', [10, 20, 30]), ('names', ['adithya', 'nagendra', 'Gummadi']), ('places', ['vja', 'hyd', 'vzg'])])
>>> a.values
...   
<built-in method values of dict object at 0x000001F2ED337F00>
