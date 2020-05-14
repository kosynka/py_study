# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона

def fibonacci(n):
    fib = [1, 2] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

summ = 0
cont = i = 0

while cont <= 4000000:
    cont = fibonacci(i)
    if cont % 2 == 0:
        summ += cont
    i += 1

print(summ)