from typing import Collection


from collections import deque


CustomQueue = deque(maxlen=3)
CustomQueue.append(1)
CustomQueue.append(2)
CustomQueue.append(3)
CustomQueue.append(3)

print(CustomQueue)
print(CustomQueue.popleft())
print(CustomQueue)
print(CustomQueue.clear())
print(CustomQueue)
