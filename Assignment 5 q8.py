lst = []
for i in range(10):
    x = int(input("Enter an integer: "))
    lst.append(x)
for _ in lst:
    if _ > 0:
        print(_, "is a positive integer")
    elif _ < 0:
        print(_, "is a negative integer")
    elif _ % 2 == 0:
        print(_, "is an even integer")
    elif _ % 2 != 0:
        print(_, "is an odd integer")
set = set(lst)
for i in set:
    print(i, "occurs", lst.count(i), "times")