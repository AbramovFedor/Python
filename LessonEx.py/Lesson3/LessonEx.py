#Определить сколько в списке встечается различныйх чисел.

import random

number = int(input())

num = []

for i in range(number):
    num.append(random.randint(3, -3))
print(num)
print(len(set(num)))

print(len(set(input().split())))
