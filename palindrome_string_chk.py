s = input("Enter a string to check palindrome : ")
rev = s[::-1]
# if string is same as reverse then it is palindrome
if s == rev:
    print(f"{s} is palindrome")
else :
    print(f"{s} is not palindrome")
