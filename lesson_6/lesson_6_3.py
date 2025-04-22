user_input = str(input("Введіть число "))

lst = []
for i in user_input:
    lst.append(int(i))

user_sum = 1
for i in lst:
    user_sum *= i

user_sum = str(user_sum)

lst_1 = []
for i in user_sum:
    lst_1.append(int(i))

user_sum_1 = 1
for i in lst_1:
    user_sum_1 *= i

user_sum_1 = str(user_sum_1)

lst_2 = []
for i in user_sum_1:
    lst_2.append(int(i))

user_sum_2 = 1
for i in lst_2:
    user_sum_2 *= i

user_sum_2 = str(user_sum_2)

lst_3 = []
for i in user_sum_2:
    lst_3.append(int(i))

user_sum_3 = 1
for i in lst_3:
    user_sum_3 *= i
print(user_sum_3)