import random

def sort_by_ins(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int


def bin_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return bin_search(array, element, left, middle - 1)
    else:
        return bin_search(array, element, middle + 1, right)


numb_str = input("Введите любую последовательность чисел через пробел: ")
element = int(input("Введите одно из чисел введеных в первом шаге: "))

numb_str = list(map(int, numb_str.split(sep=" ")))

sorted = sort_by_ins(numb_str)
print("Последовательность чисел по возрастанию): ", sorted)

element_index = bin_search(sorted, element, 0, len(sorted))
print("Индекс выбраного элемента  из отсортированнного списка: ", element_index)