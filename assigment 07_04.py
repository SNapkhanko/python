# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0

matrix_len = int(input("Enter the len of matrix"))

matrix = [x+1 if x == y else 0 for x in range(matrix_len) for y in range(matrix_len)]
print(matrix)