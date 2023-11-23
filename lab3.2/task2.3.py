from time import time
from queue import Queue

file = open('./data.txt', 'r')

startTime = time()
queue1 = Queue()
for strNum in file.readlines():
  queue1.queue.append(int(strNum))
duration = time() - startTime
print(f'Время создания очереди 1 {duration}c')
print(f'Очередь 1')
print(queue1.queue)

file.close()
file = open('./data2.txt', 'r')

startTime = time()
queue2 = Queue()
for strNum in file.readlines():
  queue2.queue.append(int(strNum))
duration = time() - startTime
print(f'Время создания очереди 2 {duration}c')
print(f'Очередь 2')
print(queue2.queue)

file.close()

startTime = time()
while len(queue1.queue) > 0 and queue1.queue[0] != 0:
  queue2.queue.append(queue1.queue.popleft())
duration = time() - startTime
print(f'Время перемещения элементов из очереди 1 в очередь 2 {duration}с')

print(f'Очередь 1')
print(queue1.queue)

print(f'Очередь 2')
print(queue2.queue)
