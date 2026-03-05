#list comprehension:every list comprehension can be re-written as a for loop but every for loop cannot be re-written in list comprehension.
#["codegnan","python","course"]
'''a=["codegnan","python","course"]
for i in a:
    print(i.upper(),end=" ")
#syntax
#a=[expr for var in collection/range]
b=[i.upper() for i in a]
print(b)'''


#problems
'''a=["python","java","ml"]
b=[i.title() for i in a]
print(b)'''
'''a=[1,2,3,5,6,8,12,13]
b=[i*i for i in a]
print(b)'''
'''a=[1,2,3,5,6,8,12,13]
b=[pow(i,2) for i in a]
print(b)'''
#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''
'''a=[i for i in range(16) if i%2!=0]
print(a)'''
#sqaure
'''a=[i*i for i in range(16) if i%2==0]
print(a)'''
#fruits
'''fruits=["apple","grapes","mango","banana","berry","kiwi","dragon"]
b=[i for i in fruits if "a" in i]
print(b)'''


#no elif usage in list comprehension
#use if else usage in list cpmpreshension
'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''
'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))
c=[a[i]+b[i] for i in range(5)]
print(c)'''


    

