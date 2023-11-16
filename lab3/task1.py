import sys
sys.path.append('..')

import inputData

steckSize = inputData.inputIntPredicate(
  f'Введите размер стека(больше 5): ',
  f'Неправильный размер',
  lambda value: value > 5
)

stack = []
for i in range(steckSize):
  stack.append(inputData.inputInt(
    f'Введите {i} числовое значение стека: ',
    f'Неправильное число'
  ))

print(f'стек')
print(stack)
print(f'адрес вершины', id(stack[len(stack)-1]))

stack.pop()
print(f'стек')
print(stack)
print(f'адрес вершины стека', id(stack[len(stack)-1]))

stack1 = []
stack2 = []
while len(stack) > 0:
  last = stack.pop()
  if last < 0:
    stack1.append(last)
  else:
    stack2.append(last)

print(f'стек 1')
print(stack1)
print(f'адрес вершины стека 1 {id(stack1[len(stack1)-1]) if len(stack1) > 0 else "nil"}')
print(f'стек 2')
print(stack2)
print(f'адрес вершины стека 2 {id(stack2[len(stack2)-1]) if len(stack2) > 0 else "nil"}')