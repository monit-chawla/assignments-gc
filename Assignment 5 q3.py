while True:
    len1 = float(input("Enter side 1: "))
    len2 = float(input("Enter side 2: "))
    len3 = float(input("Enter side 3: "))
    if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
        break
    else:
        print("Invalid side lengths")
        continue
p = (len1 + len2 + len3)/2
import math
area = math.sqrt(p * (p-len1) * (p-len2) * (p-len3))
print("The area of the triange is", area)