# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8,
# 13, 21]

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib (n-2)
my_list = []
k = int(input("Введите нужное количество: "))
for i in range(1,k+1):
    my_list.append(fib(i))
# print(my_list)
my_list_rev = sorted(my_list, reverse = True)
for i in range(len(my_list_rev)):
    if i % 2 == 0: 
        my_list_rev[i] = -my_list_rev[i]
    else:
        my_list_rev[i] = my_list_rev[i]
# print(my_list_rev)
my_list_rev.append(0)
final_list = my_list_rev + my_list
print(final_list)

    
