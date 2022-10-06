# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_dec_to_bin(dec_num:int):
    bin_num = ''
    while dec_num > 0:
        bin_num = str(dec_num % 2) + bin_num
        dec_num = dec_num//2
    print(bin_num)

dec_num = int(input("Введите число: "))
convert_dec_to_bin(dec_num)