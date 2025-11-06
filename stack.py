"""""
#initialize stack
stack=[]

#push
stack.append(554)
stack.append(23)
stack.append(78)


#pop
print(stack.pop())

#peek
print(stack[-1])

#isEmpty
print(len(stack)==0)



"""
"""""
#Using LifoQueue from queue module
from queue import LifoQueue



stack=LifoQueue()

stack.put(10)
stack.put(20)

print(stack.get())

"""

from collections import deque

stack=deque()

stack.append('B')
stack.append('A')

print(stack.pop())
