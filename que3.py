# Priority Queue example ---
# This is FIFO using priority, where lower priority 
# numbers are served before higher priority numbers.

import queue

pq = queue.PriorityQueue()
"""""
pq.put((2, "code"))
pq.put((1, "eat"))
pq.put((3, "sleep"))
while not pq.empty():
    print(pq.get()[1])
"""

pq.put((45, "low priority task"))
pq.put((78, "high priority task"))
pq.put((98, "medium priority task"))

while not pq.empty():
    print(pq.get()[1])


