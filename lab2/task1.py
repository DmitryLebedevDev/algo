count = int(input('введите количество элементов больше 0\n'))
while count <= 0:
    print('число меньше или равно 0')
    count = int(input('введите количество элементов больше 0\n'))

arr = []
for i in range(count):
    arr.append(int(input(f'введите {i} число: ')))
print(f'массив значений')
print(arr)

maxValue = 0
for v in arr:
    if (9 < v < 100 or -9 < v < -100) and v > maxValue:
        maxValue = v

if maxValue != 0:  
    print(f'максимальное двузначное значение в массиве {maxValue}')
    print(f'индекс(ы)')
    delIndex = -1
    for i in range(len(arr)):
        if arr[i] == maxValue:
            print(str(i), end=' ')
            if delIndex == -1:
              delIndex = i
        elif delIndex != -1:
            arr[delIndex] = arr[i]
            delIndex += 1
    del arr[delIndex:]
    print()
    print(f'массив после удаления максимального двузначного значения')
    print(arr)
else:
    print(f'в массиве нет двузначных значений')