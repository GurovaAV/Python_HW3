# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_dec_list = []
for i in range(len(my_list)):
    my_dec_list.append(round(my_list[i] - int(my_list[i]),2))    # отделяем дробные части
list.sort(my_dec_list)                                           # сортируем дробный части в списке
# set(my_dec_list)                                               # превращаем список в множество (в надежде на удаление неуникальных значений = 0)
if my_dec_list[0] > 0:
    res = my_dec_list[-1] - my_dec_list[0]
else:
    res = my_dec_list[-1] - my_dec_list[1]
print(res)

