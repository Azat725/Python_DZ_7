user_text = input("Введите текст: ")
reserve_words = input("Введите список слов для резервации: ")

reserved_words_list = reserve_words.split()

for word in reserved_words_list:
    user_text = user_text.replace(word, word.upper())
    
print(user_text)