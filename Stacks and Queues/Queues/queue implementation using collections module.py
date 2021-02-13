from collections import deque
# creating the queue
q = deque(maxlen=3)
print(q)
# appending values to the queue
q.append(10)
q.append(12)
q.append(14)
print(q)
q.append(16)
# overrides element instead of raising error
print(q)
# popping the first element of the queue (left side)
print(q.popleft())
print(q)
# delete / clear the entire queue
q.clear()
print(q)
