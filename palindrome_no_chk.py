n = int(input("Enter a number to check palindrome : "))
number = n
rev = 0
# separate unit's digit and then reverse the number

while(n>0):
    unit_digit = n % 10
    rev = rev*10 + unit_digit
    n = n//10

# if number is same as reverse then it is palindrome
if number == rev:
    print(f"{number} is palindrome")
else :
    print(f"{number} is not palindrome")
