#Implement stack using a list
stack = []
top = -1
max_size = int(input('Enter max size of stack'))
def push(num):
    global top
    global stack
    if top==max_size-1:
       print("Stack full.Pop to insert any more element")
       return
    top = top + 1
    stack.append(num)

def pop():
   global top
   global stack
   if top==-1:
      print("Stack empty")
      return
   top = top - 1
   element = stack.pop(len(stack)-1)

def print_stack():
   for i in reversed(stack):
      print(i)
#Stack is initially empty. Lets push few elements
push(30)
push(60)
push(120)
push(240)
pop()
print_stack()
#Empty the stack by popping all elements
pop()
pop()
pop()
print_stack()
#check for underflow
pop()
globals()
for i in range(0,max_size):
    push(12*2*i)
print_stack()
#check for overflow
push(200)