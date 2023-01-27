#Question 3

from math import factorial

n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()