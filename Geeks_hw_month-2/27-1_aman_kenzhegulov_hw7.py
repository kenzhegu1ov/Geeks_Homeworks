"""Bubble sort"""
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                print(arr)


lst = [-5, 30, 0, 6, -8]
bubbleSort(lst)
print(lst)
print('*'*50)



"""Selection sort"""
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
                (array[step], array[min_idx]) = (array[min_idx], array[step])
                print(array)


list = [-5, 30, 0, 6, -8]
size = len(list)
selectionSort(list, size)
print(list)
print('*'*50)



"""Binary search"""

list = [1, 2, 4, 6, 7, 9, 12, 15, 16, 19, 20]

def binary_search(list, val):
    first = 0
    last = len(list)-1
    ResultOk = False
    while first <= last:
        middle = (last+first)//2
        if val == list[middle]:
            first = middle
            last = first
            ResultOk = True
            Pos = middle
            if ResultOk:
                print(f'Элемент найден: {Pos}')
                break

        else:
            if val > list[middle]:
                first = middle+1
            else:
                last = middle-1

    else:
        print('Элемент не найден!')

binary_search(list, 20)
