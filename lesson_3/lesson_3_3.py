lst = []

if len(lst) % 2 == 0:
    new_lst_1 = lst[:int(len(lst) / 2)]
    new_lst_2 = lst[int(len(lst) / 2):]
    new_lst = []
    new_lst.append(new_lst_1)
    new_lst.append(new_lst_2)
    print(new_lst)
elif len(lst) % 2 != 0:
    new_lst_1 = lst[:int(len(lst) / 2 + 1)]
    new_lst_2 = lst[int(len(lst) / 2 + 1):]
    new_lst = []
    new_lst.append(new_lst_1)
    new_lst.append(new_lst_2)
    print(new_lst)
elif len(lst) == 0:
    lst.append([])
    lst.append([])
    print(lst)
