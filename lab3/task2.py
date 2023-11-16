import sys
sys.path.append('..')

import inputData

queueSize = inputData.inputIntPredicate(
  f'Введите размер очередей(больше 3): ',
  f'Неправильный размер',
  lambda value: value > 3
)

queue1 = []
for i in range(queueSize):
  queue1.append(inputData.inputInt(
    f'Введите {i} числовое значение очереди 1: ',
    f'Неправильное число'
  ))
print()
queue2 = []
for i in range(queueSize):
  queue2.append(inputData.inputInt(
    f'Введите {i} числовое значение очереди 2: ',
    f'Неправильное число'
  ))

print(f'очередь 1')
print(queue1)
print(f'адрес головы очереди 1 {id(queue1[0])}')
print(f'адрес хвоста очереди 1 {id(queue1[len(queue1)-1])}')
print(f'очередь 2')
print(queue2)
print(f'адрес головы очереди 2 {id(queue2[0])}')
print(f'адрес хвоста очереди 2 {id(queue2[len(queue2)-1])}')

while len(queue1) > 0 and queue1[0] != 0:
  queue2.append(queue1.pop(0))

print(f'очередь 1')
print(queue1)
if len(queue1) > 0:
  print(f'адрес головы очереди 1 {id(queue1[0])}')
  print(f'адрес хвоста очереди 1 {id(queue1[len(queue1)-1])}')
else:
  print(f'адрес головы очереди 1 nil')
  print(f'адрес хвоста очереди 1 nil')

print(f'очередь 2')
print(queue2)
print(f'адрес головы очереди 2 {id(queue2[0])}')
print(f'адрес хвоста очереди 2 {id(queue2[len(queue2)-1])}')
