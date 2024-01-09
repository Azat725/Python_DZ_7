def is_polindrom(string):
    reversed_string = string[::-1]
    return string == reversed_string

user_word = input("Введите строку: ")

if is_polindrom(user_word):
    print(f'<<{user_word}>> является полиндромом')
else:
    print(f"<<{user_word}>> не является полиндромом")