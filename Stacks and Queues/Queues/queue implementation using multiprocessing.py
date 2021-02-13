from multiprocessing import Queue
# creating a queue
q = Queue(maxsize=3)
# adding new values
q.put(1)
q.put(2)
# dequeueing
print(q.get())
