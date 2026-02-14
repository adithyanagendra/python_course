Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arthematic operators
a=5
b=10
print(a+b)
15
print(a-b)
-5
print(a*b)
50
print(a//b)
0
print(a/b)
0.5
print(a**b)
9765625
print(a%b)
5
#assignment operators
a=8
b=14
b+=a
b
22
b-=a
b
14
b*=a
b
112
b//=a
b
14
b/=a
b
1.75
1.75
1.75
b**=a
b
87.96388244628906
b%=a
b
7.9638824462890625
a=5
b=8
a+=b
a
13
a-=b
a
5
a*=b
a
40
a//=b
a
5
a/=b
a
0.625
a**=b
a
0.023283064365386963
a%=b
a
0.023283064365386963
a=9b
SyntaxError: invalid decimal literal
a=9
b=8
print(a+=b)
SyntaxError: invalid syntax
#comparision operators
a=7
b=8
a<b
True
b>a
True
a>=b
False
b<=a
False
a<=b
True
a!=b
True
b!=a
True
a==b
False
#logical operators
a=8
b=15
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<=b or b<=a
True
a>=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True
#identify operators
a=4
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is not int:
    print("its is not")

    

a=9
if type(a) is int:
    print("it is")

    
it is
#membership operators
a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print(10)

    
10
if 20 in a:
    print(20)

    
if 20 not in a:
    print(20)

    
20
>>> if 10 not in a:
...     print(10)
... 
...     
>>> #bitwise operators
...     
>>> a=2
>>> b=3
>>> a&b
2
>>> a|b
3
>>> a~
SyntaxError: invalid syntax
>>> ~a
-3
>>> a^b
1
>>> a=6
>>> a<<3
48
>>> a<<2
24
>>> a>>2
1
>>> a>>3
0
>>> a=5
>>> a>>3
0
>>> a=8
>>> a>>2
2
>>> a=7
>>> a>>3
0
>>> a=9
>>> a>>2
2
>>> a=11
>>> bin(11)
'0b1011'
>>> a=11
>>> a>>4
0
