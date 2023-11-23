from time import time
from collections import deque

file = open('./data.txt', 'r')

startTime = time()
stack = deque()
for strNum in file.readlines():
  stack.append(int(strNum))
duration = time() - startTime
print(f'Время создания исходного стека {duration}с')

file.close()

print(f'Cтек')
print(stack)

startTime = time()
stack1 = deque()
stack2 = deque()
while len(stack) > 0:
  last = stack.pop()
  if last == 0:
    continue
  if last < 0:
    stack1.append(last)
  else:
    stack2.append(last)
duration = time() - startTime
print(f'Время создания стеков с положительными и отрицательными значениями {duration}c')

print(f'Стек с отрицательными значениями')
print(stack1)
print(f'Стек с положительными значениями')
print(stack2)