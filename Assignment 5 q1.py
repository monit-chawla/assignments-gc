str = input("Enter the string: ")
rev_str = ""
len = len(str)
while len > 0:
    rev_str += str[len-1]
    len -= 1
print(rev_str)