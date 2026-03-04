#range():the range function returns a sequence of numbers,starting from zero by default and increments by one by one and stops before a specified numbers.
#start-stop-step
'''for i in range(10):
    print(i)'''
'''for i in range(5,15):
    print(i)'''
#5,10,15,20,25,30,35,40,45.
#2,4,6,8,10,12,14,16,18
#3,6,9,12,15,18,21,24,27
'''for i in range(5,50,5):
    print(i)'''
'''for i in range(2,20,2):
    print(i)'''
'''for i in range(3,21,3):
    print(i)'''
'''for i in range(2,20,2):
    print(i,end=" ")'''
#student grade system
'''while True:
    a=int(input("enter the value of a"))
    if a in range(0,51):
        print("failed")
    elif a in range(51,72):
        print("grade d")
    elif a in range(72,82):
        print("grade c")
    elif a in range(82,92):
        print("grade b")
    else:
        print("fail")'''
#diffrence between break continue and pass: the break statement is used to terminate the entire loop ,the continue statement is used to skips the current iteration,and rest of code will continue
#the pass statement is a null statement it does nothing but sytatically we need to use.
#break
'''a=10
while a<1:
    print(a)'''
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''
'''a=10
while a>1:
    a=a-1
    print(a)
    if a==5:
        break'''
'''for i in range(20):
    print(i)'''
'''for i in range(20):
    if i==15:
        break
    print(i)'''
#continue
'''a=30
while a>5:
    print(a)
    a=a-1'''
'''a=30
while a>5:
    a=a-1
    print(a)'''
'''a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue'''
'''a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''
'''for i in range(25):
    print(i)'''
'''for i in range(25):
    if i==20:
        continue
    print(i)'''
a="course"
'''for i in a:
    if i=="r":
        continue
    print(i)'''
#pass
'''a=30
while a>20:
      print(a)
      a=a-1'''
'''a=30
while a>20:
    print(a)
    a=a-1
    if a==15:
        pass'''
'''for i in range(8):
    if i==4:
        pass
    print(i)'''



