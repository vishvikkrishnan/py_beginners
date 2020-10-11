#Python programme to print fibonacci series

n = int(input("Enter number of terms to be printed:"))
first = 0
second = 1
for x in range(0, n ) :
  third = first + second
  print(third)
  first , second =second,third
