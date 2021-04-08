def my_title(words):
    list_words = words.split()
    return ' '.join(list(map(int_func, list_words)))


def int_func(word):
    letters = list(word)
    letters[0] = letters[0].upper()
    return ''.join(letters)

print(my_title('test func etc'))