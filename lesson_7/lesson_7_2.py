def correct_sentence(text: str) -> str:
    text_lst = list(text)
    if text_lst[-1] != ".":
        text_lst.append(".")
    if text_lst[0].islower():
        text_lst[0] = text_lst[0].upper()
    text_result = ''.join(text_lst)
    return text_result

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')