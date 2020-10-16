#this code will input a integer from user and print its reverse
num = int(input('Enter Number to reverse'))
counter = num
rev_no = 0
while counter > 0 :
    rev_no = rev_no*10
    rev_no = rev_no + counter % 10  # % is the mod operator which gives the remainder
    counter = counter // 10   # // is the Floor division operator - division that results into whole number adjusted to the left in the number line

print("reverse of the number", rev_no)   
