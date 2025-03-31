user_input = int(input("Введіть 5-x значне число: "))

number_1 = user_input // 10000
number_2 = (user_input // 1000) % 10
number_3 = (user_input // 100) % 10
number_4 = (user_input // 10) % 10
number_5 = user_input % 10

number_reverse = str(number_5) + str(number_4) + str(number_3) + str(number_2) + str(number_1)

print(number_reverse)