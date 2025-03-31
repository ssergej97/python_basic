user_input = int(input("Введіть 4-x значне число: "))

first_number = user_input // 1000
second_number = (user_input // 100) % 10
third_number = (user_input // 10) % 10
four_number = user_input % 10

print(first_number)
print(second_number)
print(third_number)
print(four_number)