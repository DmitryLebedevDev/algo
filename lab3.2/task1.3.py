from time import time
from queue import Queue

file = open('./data.txt', 'r')

startTime = time()
stack = Queue()
for strNum in file.readlines():
  stack.queue.append(int(strNum))
duration = time() - startTime
print(f'Время создания исходного стека {duration}с')

file.close()

print(f'Cтек')
print(stack.queue)

startTime = time()
stack1 = Queue()
stack2 = Queue()
while len(stack.queue) > 0:
  last = stack.queue.pop()
  if last == 0:
    continue
  if last < 0:
    stack1.queue.append(last)
  else:
    stack2.queue.append(last)
duration = time() - startTime
print(f'Время создания стеков с положительными и отрицательными значениями {duration}c')

print(f'Стек с отрицательными значениями')
print(stack1.queue)
print(f'Стек с положительными значениями')
print(stack2.queue)