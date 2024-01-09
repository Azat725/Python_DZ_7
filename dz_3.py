user_text = input("Введите текст: ")

sentences = user_text.split(". " or "? " or "! ")

num_sentances = len(sentences)

print(f"Количество предложений {num_sentances}")