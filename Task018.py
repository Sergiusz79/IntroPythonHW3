#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5 

def enter_data(text):
    try:
        a = int(input(f"Enter {text}: \n"))
    except:
        print("Error! This is not integer number!")
    return a

def search(delta_x, lst):
    close_values = []
    for i in range(len(lst)):
        if delta_x[i] == min(delta_x):
            close_values[i] = lst[i]
    return close_values    

def search_close_values(x, lst):
    delta_x = [abs(x - lst[i]) for i in range(len(lst))]
    close_values = {lst[i] for i in range(len(lst)) if delta_x[i] == min(delta_x)}
    return close_values

def print_result(close_values):
    if len(close_values) == 0 or len(close_values) == 1:
        print('Number close to given is', end=': ')
        print(*close_values)
    else:
        print('Numbers close to given is', end=': ')
        print(*close_values, sep=', ')


def task():
    n = enter_data('number of length list')
    lst = [enter_data('list item') for i in range(n)]
    x = enter_data('number to find')
    close_values = search_close_values(x, lst)
    print_result(close_values)
    
task()
