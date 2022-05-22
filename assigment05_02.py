# Завдання:

#    * запитати у користувача речення на вхід (пуста строка не приймається);
#    * відсортувати літери у кожному слові
#    * вивести результат на екран
#    * дозвольте користувачу вводити дані декілька разім (не безкінечне)
#    * ускладнене завдання: відсортуйте слова між собою (не тільки літери у словах),
#                           у спадаючому/зростаючому порядку -
#    * для саморозвитку: використайте tuple/set для зберігання літер у словах.
#                        що як убрати сортування літер у словах. чи будуть питання?
# Підказки:
#    * str.split()
#    * list(sequence), а також tuple/set конструктори
#    * reverse=True




tries = 0

while tries < 10:
    text = input("Enter your text")
    if len(text) < 1:
        print("Enter your text again")
    else:
        letters = tuple(sorted(text))
        letters_reversed = tuple(sorted(text, reverse = True))
        words = tuple(sorted(text.split()))
        words_reversed = tuple(sorted(words, reverse= True))
        print(f'{letters}\n{letters_reversed}\n{words}\n{words_reversed}')

    tries += 1
