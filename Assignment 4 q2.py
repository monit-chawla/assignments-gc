b=int(input("PLEASE ENTER THE YEAR-"))
c=b%4
d=b%100
if(c == 0):
    if(d == 0):
        print("NOT A LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")