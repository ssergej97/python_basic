lst = [12, 3, 4, 10, 8]

if len(lst) > 1:
    last_element = lst.pop(-1)
    lst.insert(0, last_element)
    print(lst)
elif len(lst) == 1 or len(lst) == 0:
    print(lst)