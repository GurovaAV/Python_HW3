# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summa_nechet(input_list: list=[]):
    summa = 0
    for i in range(1,len(input_list),2):
        summa += input_list[i]
    return(summa)
    
input_string = input('Введите элементы списка через пробел: ')
string_splitted = input_string.split(' ')            
input_list = list(map(int,string_splitted))
print(input_list)

print(summa_nechet(input_list))

