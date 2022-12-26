# Задайте число.Составьте список чисел Фибоначи, в том числе для отриц.индексов
# для = 8
# [-21,13,-8,5,-3,2,-1, 0 ,1,1,2,3,5,8,13,21]
# n = int(input('Введите число: '))
# f1 =f2 = 1
# print(f1, f2, end=' ')
# for i in range (2,n):
#     f1, f2 = f2, f2 + f1
#     print(f2, end= ' ')

# def fib(n):
#     res =[]
#     a = 0
#     b = 1
#     for __ in range(n):
#         res = res + [b]
#         a, b = b, a + b
#     return res
# n = int (input('Введите n: '))
# print(str(fib(n)))
# print(str(fib(n))[::-1]) # не работает для строки. Нужен лист

# def fib(n: int) -> list:
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 1]

#     li = fib(n-1)
#     li.append(li[-1] + li[-2])
#     return li

# n = int(input('Введите число '))

#print(fib(n)[::-1]  + fib(n)) # не выводит ноль и отриц числа



n = int(input('Введите число: '))
f1 =f2 = 1
print(f1, f2, end=' ')
for i in range (2,n):
    f1, f2 = f2, f2 + f1
    print(f2, end= ' ')
    break

for k in range(f2,0):
    





    





  
  

 
