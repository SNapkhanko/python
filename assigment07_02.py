# Є список (не пайтонівський) чисел (генерований рандомно
# чи заданий вручну) - порахувати унікальні числа у ньому
#
# Наприклад:
#  e 1, 2, 1, 3, 4, 5, 6, 6, 6
#  унікальних 6 (1 повторюється двічі, 6 тричи - три числа не враховуються)
import random

list1 = []
for i in range(10):
    list1.append(random.randint(1,10))
print(list1)
unique =[]
not_count=[]

for x in list1:
    if x not in unique:
        unique.append(x)
    else:
        dict1 = {x:list1.count(x) for x in list1}
print(f"Unique - {len(unique)} numbers" )

for k,v in dict1.items():
    if v > 1:
        print(f'{k} you can find {v} times')
    else:
        not_count.append(k)
print(f"{len(not_count)} numbers don`t count")






