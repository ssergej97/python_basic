def difference(*args) -> int | float:
    if args:
        max_of_numbers = max(args)
        min_of_numbers = min(args)

        difference_of_numbers = round(max_of_numbers - min_of_numbers, 2)
        return difference_of_numbers
    else:
        return 0

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

