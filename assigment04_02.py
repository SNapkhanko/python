# Завдання: порахуйте кількість літер у строкі. Строка та літера
#           даються на вхід користувачем. В залежності від кількости
#           виведіть на екран поясненя: строка містить літеру "с" до
#           10 разів, строка містить літеру "с" до 20 разid, строка містить
#           символ "c" більше 20 разів. Проінформуйте користувача якщо
#           введено більше ніж одну літеру або повідомляти якщо такої літери
#           взагалі не знайдено. Програма повинна використовувати
#           інструкцію цикла для ітерації літер строки (не через метод str).
#           Програма повинна дозволяти користувачу вводити данні до 10 разів
#           (як попередня програма але лімітувати кількість можливостей).
#
# Приклад:
#
# Введіть текст: Це якийсь рандомний текст
# Введіть літеру: й
# Строка містить літеру "й" до 10 разів.
#
# Введіть текст: аааааааааааааааааааааааа
# Введіть літеру: а
# Строка містить літеру "а" більше 20 разів.



tries = 0

while tries <= 10:
    a = input("Enter your text")
    b = input("Enter your letter")
    text = a.lower()
    letter = b.lower()
    tries += 1

    for x in text:
        count_text = text.count(letter)
        for y in letter:
            len_letter = len(letter.lower())
    if len_letter > 1:
        print("You enter more the one letter")
    elif count_text <= 0:
        print(f"Letter {letter} doesn`t find")
    elif count_text <= 10:
        print(f"String has the letter {letter} till 10 times")
    elif count_text <= 20:
        print(f"String has the letter {letter} till 20 times")
    else:
        print(f"String has the letter {letter} more 20 times")
if tries >= 10:
    print("You make over 10 tries")