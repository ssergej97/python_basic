user_input_num1 = int(input("Введіть перше число "))
user_input_num2 = int(input("Введіть друге число "))
user_input_calc = input("Введіть дію над цими числами ")

if user_input_calc == "+":
    user_input_result = user_input_num1 + user_input_num2
    print("Ваш результат ",user_input_result)
elif user_input_calc == "-":
    user_input_result = user_input_num1 - user_input_num2
    print("Ваш результат ", user_input_result)
elif user_input_calc == "*":
    user_input_result = user_input_num1 * user_input_num2
    print("Ваш результат ",user_input_result)
elif user_input_calc == "/":
    if user_input_num2 == 0:
        print("На нуль ділити не можна!")
    else:
        user_input_result = user_input_num1 / user_input_num2
        print("Ваш результат",user_input_result)
else:
    print("Ви ввели неправильну дію. Введіть +, -, * або /")

