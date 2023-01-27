#Question 1

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(Number," is a perfect number")
else:
    print(Number," is not a perfect number")
