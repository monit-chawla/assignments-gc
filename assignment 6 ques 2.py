#Question 2

def palindrome(string):
    rev_string=string[::-1]
    print(rev_string)
    if string==rev_string:
        print("entered string is a palindrome")
    else:
        print("entered string is not a palindrome")

user_string=str(input("enter a word, phrase or sentence: "))
palindrome(user_string)