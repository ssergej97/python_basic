def difference(*args) -> int | float:
    list_of_numbers = []

    for number in args:
        list_of_numbers.append(number)

    if len(list_of_numbers) == 0:
        return 0

    max_of_numbers = max(list_of_numbers)
    min_of_numbers = min(list_of_numbers)

    difference_of_numbers = max_of_numbers - min_of_numbers

    if isinstance(difference_of_numbers, float):
        difference_of_numbers = round(difference_of_numbers, 2)
        return difference_of_numbers
    else:
        return difference_of_numbers
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')