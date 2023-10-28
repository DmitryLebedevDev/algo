import random
import math

count = int(input('введите количество элементов больше 0\n'))
while count <= 0:
    print('число меньше или равно 0')
    count = int(input('введите количество элементов больше 0\n'))

valueFrom = int(input('введите начальную границу диапазона для генерирующихся чисел\n'))
valueTo = int(input('введите конечную границу диапазона для генерирующихся чисел\n'))
while valueFrom > valueTo:
    print('нижняя граница больше конечной границы')
    valueFrom = int(input('введите начальную границу диапазона для генерирующихся чисел\n'))
    valueTo = int(input('введите конечную границу диапазона для генерирующихся чисел\n'))

arr = []
for i in range(10):
    arr.append(random.randint(valueFrom, valueTo))
print(f'массив значений')
arr.sort()
print(arr)

findKey = int(input(f'введите ключевое число\n'))
left = 0
right = len(arr)-1
while left <= right:
    mid = math.floor((left + right)/2)
    if arr[mid] >= findKey:
        right = mid - 1
    else:
        left = mid + 1
if left < len(arr) and arr[left] == findKey:
    print(f'индекс(ы) ключевых чисел')
    while left < len(arr) and arr[left] == findKey:
        print(str(left) + ' ')
        left += 1
else:
    print('ключевые числа не найдены')