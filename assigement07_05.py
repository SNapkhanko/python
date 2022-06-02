# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#

N = int(input("Enter N"))
K  = int(input("Enter K, K should be smaller than N"))
if K > N:
    K = round(int(N*(K*0.01)))


list1 = [x for x in range(N+1) if x % K != 0]
print(list1)