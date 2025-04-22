import string

# user_input = input("Введіть дві літери через дефіс, наприклад, a-c ")

lst = []

for i in user_input:
    if i in string.ascii_letters:
       lst.append(i)

letter_1 = lst[0]
letter_2 = lst[1]

ascii_only = ''.join(string.ascii_letters)

ascii_2_index = 1

for i in ascii_only:
    if i == letter_1:
        ascii_1_index = ascii_only.index(i)
    elif i == letter_2:
        ascii_2_index = ascii_only.index(i) + 1


ascii_lst = []
for i in ascii_only:
    ascii_lst.append(i)

user_string = ascii_lst[ascii_1_index:ascii_2_index]
user_string_final = ''.join(user_string)
print(user_string_final)

