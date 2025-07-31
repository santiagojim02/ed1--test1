import random

list = []

for i in range(0,10):
    list.append(random.random())


total = 0
for num in list:
    total += num
print(total)