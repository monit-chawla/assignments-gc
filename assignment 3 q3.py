list1=list(map(int,input("Enter the numbers separated due to space:").split()))
#blank list
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
# Printing the final result
print("\nList containing (n,n^2) is shown below:")
print(list2)
