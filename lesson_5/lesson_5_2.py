user_input_num1 = int(input("Введіть перше число "))
user_input_num2 = int(input("Введіть друге число "))
user_input_calc = input("Введіть дію над цими числами ")

if user_input_calc == "+":
    user_input_result = user_input_num1 + user_input_num2
    print("Ваш результат ",user_input_result)
    user_input_cont = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
elif user_input_calc == "-":
    user_input_result = user_input_num1 - user_input_num2
    print("Ваш результат ", user_input_result)
    user_input_cont = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
elif user_input_calc == "*":
    user_input_result = user_input_num1 * user_input_num2
    print("Ваш результат ",user_input_result)
    user_input_cont = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
elif user_input_calc == "/":
    if user_input_num2 == 0:
        print("На нуль ділити не можна!")
    else:
        user_input_result = user_input_num1 / user_input_num2
        print("Ваш результат",user_input_result)
        user_input_cont = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
else:
    print("Ви ввели неправильну дію. Введіть +, -, * або /")

user_input_continue = "yes"

while user_input_continue == "yes":
    user_input_new_num = int(input("Введіть нове число "))
    user_input_new_calc = input("Введіть дію над числами ")
    if user_input_calc == "+":
        user_input_result = user_input_result + user_input_new_num
        print("Ваш результат ", user_input_result)
        user_input_continue = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
    elif user_input_calc == "-":
        user_input_result = user_input_result - user_input_new_num
        print("Ваш результат ", user_input_result)
        user_input_continue = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
    elif user_input_calc == "*":
        user_input_result = user_input_result * user_input_new_num
        print("Ваш результат ", user_input_result)
        user_input_continue = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
    elif user_input_calc == "/":
        if user_input_new_num == 0:
            print("На нуль ділити не можна!")
        else:
            user_input_result = user_input_result / user_input_new_num
            print("Ваш результат", user_input_result)
            user_input_continue = input("Ви бажаєте продовжити обчислення? Введіть yes або no ")
    else:
        print("Ви ввели неправильну дію. Введіть +, -, * або /")