# Напишите прграмму, которая будет преобразовывать десятичное число в двоичное
# 45 ->101101
# 3 -> 11
# 2 -> 10

# x = int(input("Введите натуральное число: "))
# n = ""
 
# while x > 0:
#  n = str(x % 2)+ n
#  x = x // 2
 
#print (n) #101101

n = 45
a = []
for i in range(len(a)):
    x = n%2
    a.append(x)
    n//2
    print(a) # []   не работает
             