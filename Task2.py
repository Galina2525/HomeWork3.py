#Напишите прграмму, которая найдет произведение пар чисел списка.
#Парой считается первый и последний элемент, второй и предпоследний и т.д
# [2,3,4,5,6 ]->[12,15,16]
# [2,3,5,6 ]->[12,15,]
my_list = [1, 2, 5, 3]
def fun (list_):
    list2 = []
    mult = 1
    
    for i in range(len(list_)//2 + len(list_)%2):# или (len(list)+1)//2
        mult = list_[i] * list_[len(list_)-i-1]
        list2.append(mult)
    print(list2)
    
      

fun(my_list)        


        
        