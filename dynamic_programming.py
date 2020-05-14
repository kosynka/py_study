# Вывод чисел Фибоначи с помощью динамического программирования
def fibonacci(n):
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
# print(fibonacci(100))


# A = [[0]*M for i in range(N)]  -  Создание двумерного массива


# Найти макс длину подпоследовательности из двух массивов A & B:
def largest_common_subsequence(A, B):
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    print (F[-1][-1])
# largest_common_subsequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 9])


# Алгоритм редакционного расстояния Левенштейна
def levenstein(A, B):
    F = [[i+j if i*j == 0 else 0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(A)][len(B)]
# a = 'молоко'
# b = 'колокол'
# print(levenstein(a,b))


# Алгоритм Кнута-Морриса-Прата. Через префикс фунцию ищем префиксное слово в словаре
def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p
# print(prefix('игла@сеноиглсенигласенменоиглаигла'))


