def eratosthenes(n):
    """ Алгоритм нахождения простых чисел по методу Решето Эротосфена,
        где n - число, до которого хотим найти простые числа
    """
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

print(eratosthenes(200))

# List Comprehensive, создание динамического массива(листа), который работает быстрее
A = [1, 2, 3, 4, 7, 8, 4, 20, 11, 9, 6, 5]
B = []

for x in A:
    if x % 2 == 0:
        B.append(x**2)

C = [x**2 for x in A if x%2==0]
# тут C и B равны, но второй вариант работает быстрее и пишется компактнее, 
# но теряет читабельность при очень длинных случаях

# квадратичные сортировки/O(N^2):
A = [4, 2, 5, 1, 3]
# 1-insertion sort/вставками
def insert_sort(A):
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

# 2-select sort/выбора
def select_sort(A):
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

# 3-bubble sort/пузырька
def bubble_sort(A):
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]



# Сортировка подсчетам - count sort/O(N)
N = int(input())
F = [0] * 10

for i in range(N):
    x = int(input())
    F[x] += 1


# Алгоритм Эвклида
def gcd(a, b):
    """ Алгоритм быстрого нахождения Наибольшего
        общего делителя между a и b
    """
    return a if b==0 else gcd(b, a % b)


# Ханойские башни

def hanoi(n:int, first:int, final:int):
    """ Рекурсивный алгоритм для решения задачи Ханойских башен
        Правила: есть 3 стержня и башня высотой n дисков. Нужно
        переложить пирамиду из стержня first на final, можно за
        раз брать только один стержень и нельзя ставить больший
        диск на меньшую.
    """
    if (n == 1):
        print('move disk ' + n + ' from ' + first + ' to ' + final)
    else:
        tmp = 6 - first - final
        hanoi(n-1, first, tmp)
        print('move disk ' + n + ' from ' + first + ' to ' + final)
        hanoi(n-1, tmp, final)


# Рекурсивный метод перебирания всех чисел/все равно что дедуктивный
def generate_num(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-ричной системе счисления (N <= 10) длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_num(N, M-1, prefix)
        prefix.pop()


# Рекуррентные сортировки:
# Сортировка слиянием
def merge(A:list, B:list):
    C = 0 * (len(A) + len(B))
    i = k = n = 0
    while i<len(A) and k<len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i<len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k<len(B):
        C[n] = B[k]
        i += 1
        n += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    left = [A[i] for i in range(0, middle)]
    right = [A[i] for i in range(middle, len(A))]
    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    for i in range(len(A)):
        A[i] = C[i]

# num = [5, 1, 9, 7, 3, 1, 8]
# merge_sort(num)
# print(*num)

# Сортировка Тони Хоара
def hoart_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    left = []
    middle = []
    right = []
    for x in A:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    hoart_sort(left)
    hoart_sort(right)
    k = 0
    for x in left+middle+right:
        A[k] = x
        k += 1

# бинарный поиск левой границы определенного числа
def left_bound(A, key):
    left = -1
    right = len(A)
    while right-left>1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left