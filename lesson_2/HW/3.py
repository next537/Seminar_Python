# 3. Задайте список из n чисел, заполненный по формуле
# (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
n = int(input("Введите число: "))
for i in range(1, n + 1):
    num_list.append(round(((1 + 1 / i) ** i), 3))
print(num_list)
print(sum(num_list))
