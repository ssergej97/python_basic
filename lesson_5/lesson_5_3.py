import string

user_input = input("Ввeдіть слово ")

for i in user_input:
    if i in string.punctuation:
        user_input = user_input.replace(i, "")

user_input = user_input.title()

for i in user_input:
    if i == ' ':
        user_input = user_input.replace(i, "")

user_input_list = list(user_input)

user_input_list.insert(0, "#")
hashtag = ''.join(user_input_list)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)


