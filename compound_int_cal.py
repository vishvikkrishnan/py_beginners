
#This program is to find compound interest for principal amount - all inputs are taken from user.

# This method is to find Compound interest
def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result

# Taking inputs from user

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))

amount = compound_interest(principal_amount, rate_of_interest, time)
interest = amount - principal_amount
print("Compound amount is %.2f" % amount)
print("Compound interest is %.2f" % interest)



