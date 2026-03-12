#variable length arguments:this arguments are automatically stores in tuple and we use star *arguments.
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(d)
e={3,4,5,6,7}
check(*e)
f={"name":"pooja","city":"vja"}
check(*f)'''

'''def check1(*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i)==int or  type(i)==float:
        #if type(i) is (int,float):    it is one more method to consider int and float 
          d=d+i
          print(d)
        
check1()
check1(2,3,4,5,6)
check1(2,3,4,3.5,6.2,4.3)
check1(1,3,5,6.2,3.2,"adithya")'''



#kwargs(**) arguments
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],"names":["somanth","adithya","mahesh"],"status":["p","A","P"]}
details(**d)'''



'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30],"names":["somanth","adithya","mahesh"],"status":["p","A","P"]}
details(**d)'''

#* arguments and ** arguments in one code usage
def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
final()
data=(2,3,4,5,2.3,4.5)
final(*data)
details={"idnos":[10,20,30],"names":["somanth","adithya","mahesh"],"status":["p","A","P"]}
final(**details)
final(*data,**details)



