import random

num = 90
row = num // 10
col = num % 10

for i in range(-1, 2, 1):
    # row += i
    # print(row + i)
    for j in range(-1, 2, 1):
        # print(i+j)
        # col += j
        # print(row+i, col+j)
        if 10 > row+i >= 0 and 10 > col+j >= 0:
            print(row+i, col+j)
