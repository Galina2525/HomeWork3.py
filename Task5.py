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



number_ = int(input('Введите число: '))
def fibonacci(num):
    list_fib = [0, 1]
    num1 = 0
    num2 = 1
    i = 2
    while i <= (num * -1):
        fib = num1 + num2
        list_fib.append(fib)
        num1 = num2
        num2 = fib
        i+=1
    return list_fib

list_fibonacci = fibonacci(number_)   

def fibonacci_neg(num, list_f):
    list_fib_neg = []
    for x in range(num, 0):
        result = pow(-1),(x+1) * list_f[x] # меняем знаки чере элемент
        list_fib_neg.append(round(result))
    return list_fib_neg

list_fibonacci_neg = fibonacci_neg(number_, list_fibonacci)
list_fibonacci_neg.reverse()

print(list_fibonacci_neg + list_fibonacci)


    





    





  
  

 
