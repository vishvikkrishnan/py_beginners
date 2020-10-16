n= int(input('Enter Number to reverse'))
i = n
m  = 0
while i>0:
    m = m*10
    m = m + i%10
    i = i//10

print(m)
