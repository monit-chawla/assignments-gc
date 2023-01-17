import random
a=[0,1,2,3,4,5,6,7,8,9,10]
for c in range(0,10):
    e=random.choice(a) 
    f=random.choice(a)
    print(e,"X",f)
    b=int(input())
    if(b==e*f):
        print("RIGHT!")
    else:
        print("Wrong.The answer is ",e*f)