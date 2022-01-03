import queue as q


CustomQueue = q.Queue(maxsize=3)
CustomQueue.put(1)
CustomQueue.put(2)
CustomQueue.put(3)
# CustomQueue.put(3)
print(CustomQueue.qsize())