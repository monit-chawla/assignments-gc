n = 6
for i in range(n):
    # print spaces
    for j in range(i):
        print(' ', end='')
    # print alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()
