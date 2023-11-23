from time import time 

file = open('./data.txt', 'r')

startTime = time()
queue1 = []
for strNum in file.readlines():
  queue1.append(int(strNum))
duration = time() - startTime
print(f'Время создания очереди 1 {duration}c')
print(f'Очередь 1')
print(queue1)

file.close()
file = open('./data2.txt', 'r')

startTime = time()
queue2 = []
for strNum in file.readlines():
  queue2.append(int(strNum))
duration = time() - startTime
print(f'Время создания очереди 2 {duration}c')
print(f'Очередь 2')
print(queue2)

file.close()

startTime = time()
while len(queue1) > 0 and queue1[0] != 0:
  queue2.append(queue1.pop(0))
duration = time() - startTime
print(f'Время перемещения элементов из очереди 1 в очередь 2 {duration}с')

print(f'Очередь 1')
print(queue1)

print(f'Очередь 2')
print(queue2)
