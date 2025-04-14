import string
import keyword

user_input = input("Enter your name ")

check_is_upper = False

for i in user_input:
    if i.isupper():
        check_is_upper = True

for i in user_input:
    if i.isspace():
        check_is_upper = True
    elif i in string.punctuation and i != "_":
        check_is_upper = True

if user_input[0].isdigit():
    print("False")
elif user_input in keyword.kwlist:
    print("False")
elif user_input.count("_") > 1:
    print("False")
elif check_is_upper:
    print("False")
else:
    print("True")



