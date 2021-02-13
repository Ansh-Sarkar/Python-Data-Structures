import queue as q
# creating the queue
queue=q.Queue(maxsize=3)
print(queue.qsize())
print(queue.empty())
# appending , enqueue()
queue.put(1)
queue.put(2)
queue.put(3)
# check whether the queue is full
print(queue.full())
# dequeue method
print(queue.get())
# returns a Queue type object
print(queue)
# check the size of the queue
print(queue.qsize())


