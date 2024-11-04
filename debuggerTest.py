def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]

    return num 
numers = [5,18,7,2,6,8,9]
print(bubble_sort(numers))

def count(n):
    if n == 0:
        return 
    count(n-1)
    print(n)
# count(5)

def recursionSumation(inputNumber):
    if inputNumber <= 1:
        return inputNumber
    return inputNumber+recursionSumation(inputNumber-1)
print(recursionSumation(10))
def binarySearch(a, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2  # Use divisão inteira para obter um índice válido
    if x == a[mid]:
        return mid
    if x < a[mid]:
        return binarySearch(a, left, mid - 1, x)
    return binarySearch(a, mid + 1, right, x)

# Lista ordenada
array = [1, 3, 5, 7, 9, 11, 14, 15]

# Elemento a ser encontrado
x = 14

# Chamada da função
index = binarySearch(array, 0, len(array) - 1, x)
print(index)  # Saída: 3 (porque 7 está na posição 3 da lista)
# https://www.youtube.com/watch?v=IJDJ0kBx2LM (recursion)