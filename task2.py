# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

input_string = input('Введите элементы списка через пробел: ')
string_splitted = input_string.split(' ')            
input_list = list(map(int,string_splitted))
# print(input_list)

def pairs_multiply(input_list: list=[]):
    multiplied_list = []
    i = 0
    if len(input_list) % 2 == 0:        # для списков с четным числом элементов
        while i < len(input_list)//2:
            multiplied_list.append(input_list[i] * input_list[len(input_list)-1-i])
            i += 1
        return(multiplied_list)
    else:                               # для списков с нечетным числом элементов
        while i <= len(input_list)//2:
            multiplied_list.append(input_list[i] * input_list[len(input_list)-1-i])
            i += 1
        return(multiplied_list)

print(pairs_multiply(input_list))