def find_unique_value(some_list: list) -> int | float:
    unique_lst = [i for i in some_list if some_list.count(i) == 1]
    if type(unique_lst[0]) == int:
        unique_num = int(''.join(str(i) for i in unique_lst))
        return unique_num
    else:
        unique_num = float(''.join(str(i) for i in unique_lst))
        return unique_num
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

