def second_index(text: str, some_str: str) -> int:
    indexes = []
    start = 0
    while True:
        index = text.find(some_str, start)
        if index == -1:
            break
        indexes.append(index)
        start = index + 1

    if len(indexes) <= 1:
        indexes.append(None)

    return indexes[1]
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
