input_string=input("Enter string with hyphen seperated sequence :")
items=input_string.split('-')
items.sort()
print('-'.join(items))