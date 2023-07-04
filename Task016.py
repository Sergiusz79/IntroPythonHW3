# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

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
    i = 0
    n = enter_data('number of length list')
    lst = [enter_data('list item') for i in range(n)]
    x = enter_data('number to find')
    count = count_x_in_list(x, lst)
    print(f'The number {x} occurs {count} times in list.')

task()
