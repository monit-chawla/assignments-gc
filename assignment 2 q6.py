line1 = int(input("enter your 1st line :"))
line2 = int(input("enter your 2nd line :"))
line3 = int(input("enter your 3rd line :"))
if line1 == (line2 +line3):
    print("no, formation of triangle is not possible")
elif line2 == (line1+line3):
    print("no, formation of triangle is not possible")
elif line3 ==(line2 +line1):
    print("no, formation of triangle is not possible")
elif line1 < (line2 +line3):
    print("yes, formation of triangle is possible")
elif line2 < (line1 +line3):
    print("yes, formation of triangle is possible")
elif line3 < (line2 +line1):
    print("yes, formation of triangle is possible")

else:
    print("no, formation of triangle is not possible")
