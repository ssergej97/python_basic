import string

def is_palindrome(text: str) -> bool:
    text_new = ''.join(i for i in text if i not in string.punctuation)

    text_new = text_new.lower()
    text_new = text_new.replace(" ", "")

    text_reversed = ''.join(reversed(text_new))

    if text_new == text_reversed:
        return True
    else:
        return False
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")





