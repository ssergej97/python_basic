def second_index(text: str, some_str: str) -> int | None:
    x = 0

    for i in range(len(text)):
        if text.startswith(some_str, i):
            x += 1
            if x == 2:
                return i
                break

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')




