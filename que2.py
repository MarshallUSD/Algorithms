

# Using deque to use DS as queue
"""""
from collections import deque

q=deque()

q.append('A')
q.append('B')
q.append('C')

print(q.popleft()) # A

"""
# Using list to use DS as queue
"""""
queue=[]

queue.append('C&C generals')
queue.append('Age of empires')
queue.append('Fifa 2024')

print(queue.pop(0))

"""
# Using Queue from queue module 

from queue import Queue

q=Queue()

q.put('C&C generals')
q.put('Age of empires')
q.put('Fifa 2024')


print(q.get())
