lst = [6]

sum_of_lst = 0

if len(lst) > 0:
    for i, el in enumerate(lst):
        if i % 2 == 0:
            sum_of_lst += el
    sum_of_lst *= lst[-1]
print(sum_of_lst)
