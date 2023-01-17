def div_num(lr, ur):
    n = int(input("Enter the number: "))
    for _ in range(lr, ur + 1):
        if _ % n == 0:
            print(_)
div_num(int(input("Enter the lower range: ")), int(input("Enter the upper range: ")))