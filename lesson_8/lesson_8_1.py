def add_one(some_list: list) -> list:
    some_list = list(map(str, some_list))
    num_string = int(''.join(some_list))
    num_string += 1
    new_lst = list(str(num_string))
    new_lst = list(map(int, new_lst))
    return new_lst
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")