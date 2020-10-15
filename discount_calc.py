

#This program is to find price after discount - default 10 per and price is taken from user as input

price = float(input("Enter price amount:"))
discount = 10
output = price - (price * discount / 100)
print("After discount your price is: ", output)



#This program is to find price after discount - Both Price and discount is taken from user as inputs

price = float(input("Enter price amount:"))
discount = float(input("Enter discount percentage:"))
output = price - (price * discount / 100)
print("After discount your price is: ", output)