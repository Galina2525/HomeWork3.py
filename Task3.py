# Задайте список из вещественных чисел.
# Напишите программу, которая найдет разницу между макс и мин значением
# дробной части элементов
#[1.1, 1.2, 3.1, 10.01] -> 0.19

# my_list = [1.1, 1.2, 3.1, 10.01] 
# def fun(list_):
#     min_ = list_[0] % 1
#     max_ = list_[0] % 1
#     for i in range(len(list_)):
#         if list_[i] % 1> max_:
#             max_ = list_[i] % 1
#         if list_[i] %1 < min_:
#             min_ = list_[i] % 1
         
#     print(round (max_ - min_, 2))  
# fun(my_list)      
# или
my_list = [1.1, 1.2, 3.1, 10.01] 
def fun (list_):
    new_list = []
    for i in range (len(list_)):
        n = list_[i] % 1
        new_list.append(n)
        my_min = min(new_list)
        my_max = max(new_list)
    print(round(my_max - my_min, 2))
fun(my_list)      

