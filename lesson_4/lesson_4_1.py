lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for i in lst:
    if i == 0:
        ind = lst.index(0)
        lst.append(lst.pop(ind))

print(lst)