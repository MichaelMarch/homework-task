import math

rows = 9 

first_batch_count = math.ceil(rows / 2.0)

for i in range(0, first_batch_count):
    print('* ' * (i + 1))

for i in range(rows - first_batch_count, 0, -1):
    print('* ' * i)