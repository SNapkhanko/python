# Завдання:
#     * згенерувати лист з рандомними числами (числа від 50 до 100 кожне,
#       довжину листа запитати у користувача, але не коротший за 10 та не
#       довший за 50 елементів;
#     * відсортувати елементи в убуваючому порядку (10, 9, 8...)
#     * напечатати на екран
#     * додати можливість циклічного вводу даних для експеріментів
#
#     * ускладнене завдання: написати та використати bubble-sort алгоритм
#
# Підказки:
#     * .sort()
#     * reverse=True

import random

l = []
while True:
    len_string = int(input("Enter the len of string from 10 till 50"))
    if len_string == 'quit':
        break
    for x in range (len_string):
        l.append(round(random.random() * 100 % 50))
        for a in range(len(l)):
            for b in range(a+1, len(l)):
                if l[a] < l[b]:
                    tmp = l[a]
                    l[a]= l[b]
                    lb = tmp
    print(l)

