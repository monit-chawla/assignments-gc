ur = int(input("Enter the upper range: "))
print("The prime numbers in the given range are")
for _ in range(2, ur + 1):
    for j in range(2, _):
        if _ == j:
            pass
        elif _ % j == 0:
            break
    else:
        print(_, end=", ")