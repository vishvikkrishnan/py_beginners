# simple queue data structure with CRUD
class Queue:

  def __init__(self):
    self.data = []

  def is_empty(self):
    return len(self.data) == 0 # self.data == []

  def enqueue(self, value): # insert
    self.data.insert(0, value)

  def dequeue(self): # delete
    if self.is_empty():
      return "Cannot delete from empty queue"
    return self.data.pop()

  def size(self):
    return len(self.data)

  def display(self):
    if self.is_empty():
      print("Empty queue")
    else:
      print("Contents: ", end='')
      #for i in range(len(self.data)): # printing from rear to front
      for i in range(len(self.data)-1, -1, -1):
        print(self.data[i], end=' ')
      print()
