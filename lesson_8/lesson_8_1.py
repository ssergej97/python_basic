def add_one(some_list: list) -> list:
    for index, value in enumerate(some_list):
        some_list[index] = str(value)
    num_string = int(''.join(some_list))
    num_string += 1
    new_lst = list(str(num_string))
    for index, value in enumerate(new_lst):
        new_lst[index] = int(value)
    return new_lst
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")