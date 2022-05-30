# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.

text = input ("Enter your text")

text_split = text.split()

words = {i : text_split.count(i) for i in text_split}
letters = {i: text.count(i) for i in text}

print(f' In your text was found next letters {letters}')
print(f' In your text was found next words {words} ')
