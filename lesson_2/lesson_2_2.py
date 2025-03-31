user_input = int(input("Введіть 5-x значне число: "))

number_1 = user_input // 10000
number_2 = (user_input // 1000) % 10
number_3 = (user_input // 100) % 10
number_4 = (user_input // 10) % 10
number_5 = user_input % 10

number_reverse = number_5 * 10000 + number_4 * 1000 + number_3 * 100 + number_2 * 10 + number_1

print(number_reverse)