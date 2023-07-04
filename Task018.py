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

def count_x_in_list(x, lst):
    count = 0
    for i in range(len(lst)):
        if x == lst[i]:
            count +=1
    return count

def task():
    n = enter_data('number of length list')
    lst = [enter_data('list item') for i in range(n)]
    x = enter_data('number to find')
    count = count_x_in_list(x, lst)
    print(f'The number {x} occurs {count} times in list.')

task()
