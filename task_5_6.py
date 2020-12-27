""" Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего). [02-4.1-ML27]"""
lst = [1, 2, 3, 4, 5, 6, 0, 15, 20, 30, 4, 10, 15, 16, 17, 3, 2, 1]
interval_count = 0
intermediate_result = 0
for i in range(len(lst) - 1):
    a = lst[i]
    b = lst[i + 1]
    if a < b:
        intermediate_result += 1
        continue
    else:
        if intermediate_result != 0:
            interval_count += 1
            intermediate_result = 0
print(interval_count)