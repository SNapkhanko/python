# Завдання:

#    * згенерувати лист з рандомними числами (числа від 50 до 100 кожне,

#      довжину листа запитати у користувача, але не коротший за 10 та не

#      довший за 50 елементів;

#    * порахувати кількість елементів списку які більше обох своїх сусідніх

#      (зліва та справа)
import random
len_list = int(input("Enter the len of list"))
list1 =[]
counter = 0
if 10 < len_list < 50:
    for x in range(len_list):
        list1.append(random.randint(50, 100))
    for a in range (1, len(list1)-1) :
        if list1[a-1]< list1[a] >list1[a+1]:
            counter +=1
    print(list1)
    print(counter)
else:
    print("You enter the wrong len should be more than 10 and less the 50")


