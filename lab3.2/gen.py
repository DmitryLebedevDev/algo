import random

file = open('data2.txt', 'w+')

file.write('\n'.join([
  str(random.randint(-100, 100)) for _ in range(100)
]))

file.close()
