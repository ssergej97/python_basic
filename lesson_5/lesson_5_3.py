import string

user_input = input("Ввeдіть слово ")
user_input = user_input.title()

user_input_list = list(user_input)

for i in user_input_list:
    if i in string.punctuation:
        user_input_list.remove(i)
    elif i == ' ':
        user_input_list.remove(i)

user_input_list.insert(0, "#")
hashtag = ''.join(user_input_list)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)


