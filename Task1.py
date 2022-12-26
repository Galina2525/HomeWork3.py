# Задайте список из нескольких чисел. Напишите программу, которая найдет
# сумму элементов списка, стоящих на нечетной позиции

# sum = 0
# i = 1
# while i < len(my_list):
#     s += my_list[i]
#     i += 2
# print(s)

my_list = [3, 5, 6, 8, 9, 4]

def fun(list_):
    s = 0
    for x in range(len(list_)):
        if x % 2 != 0:
             s = s + list_[x]
    print(s)      

fun(my_list)            

