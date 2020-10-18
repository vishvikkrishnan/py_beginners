correct_ans= 0
questions = 3

print("**************Quiz***************")
print("---Start---")

print("1. When is the Independence Day celebrated in United State of America?")
print("""a. 25th December
b. 22nd November
c. 1st May
d. 4th July""")
answer = input()

if answer == "d":
  correct_ans += 1
  print("Correct")
else:
  print("Incorrect")
  
print("")

print("2. Who is the president of United States of America")
print("""a. Donald J Trump
b. Barack Obama
c. Joe Biden
d. Kamala Harris""")

answer = input()

if answer == "a":
  correct_ans += 1
  print("Correct")
else:
  print("Incorrect")
  
print("")

print("3. When are elections held in United States of America")
print("""a. The first Tuesday after November 1st
b. The first Monday after May 1st
c. The first Friday after September 1
d. The last Tuesday in November """)

answer = input()

if answer == "a":
  correct_ans += 1
  print("Correct")
else:
  print("Incorrect")
  
print("")

score = round(correct_ans/questions*100)
print("---Done----")
print("You scored a "+str(score)+"%")


