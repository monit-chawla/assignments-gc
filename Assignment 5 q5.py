x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = int(input("Enter the number of rows: "))
y, c = 0, 1
for _ in range(1, 1+r):
    print(x[y:c])
    y = c
    c += _ + 1