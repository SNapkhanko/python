# Завдання:

#    * згенерувати лист з рандомними числами (числа від 50 до 100 кожне,

#      довжину листа запитати у користувача, але не коротший за 10 та не

#      довший за 50 елементів;

#    * порахувати кількість елементів списку які більше обох своїх сусідніх

#      (зліва та справа)
import random
len_list = int(input("Enter the len of list"))
list1 =[]
list2 = []
for x in range(len_list):
    list1.append(random.randint(50, 100))
    print(list1)
    #for y in list1:
        #if list1[y] > list1[y+1]:
            #list2.append(y)


