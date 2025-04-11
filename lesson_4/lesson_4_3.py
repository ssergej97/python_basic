import random

lst = []

tup = range(random.randint(3, 11))

for i in tup:
    lst.append(random.randint(3, 10))

print(lst)

new_lst = []

new_lst.append(lst[0])
new_lst.append(lst[2])
new_lst.append(lst[-2])

print(new_lst)
