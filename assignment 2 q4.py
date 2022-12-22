num1 = int(input("enter your 1st number :"))
num2 = int(input("enter your 2nd number :"))
num3 = int(input("enter your 3rd number :"))
if num1>num2 and num1>num3:
    print(f"{num1} is greatest")
elif num2>num3 and num2>num1:
    print(f"{num2} is greatest")
elif num3>num1 and num3>num2:
    print(f"{num3} is greatest")
elif num2== num3 and num3==num1:
    print("all numbers are equal")
elif num1 ==num2:
    print(f"number 1 and 2 both are equal")
elif num2 == num3:
    print("number 2 and 3 both are equal")
elif num1 ==  num3:
    print("number 1 and 3 both are equal")
else:
    print(f"{num3} is greatest")
