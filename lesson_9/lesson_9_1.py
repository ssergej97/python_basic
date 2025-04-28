def popular_words (text: str, words: list) -> dict:
    text_lower = text.lower()
    text_lower_split = text_lower.split()
    numbers_of_words = {word: 0 for word in words}

    for i in text_lower_split:
        if i in words:
            numbers_of_words[i] += 1

    return numbers_of_words
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')






