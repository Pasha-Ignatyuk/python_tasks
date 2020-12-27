"""Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]"""
#  Два числа называются дружественными, если они имеют одинаковую сумму всех делителей, равную сумме этих двух чисел.
max_number = 300

# Функция возвращает сумму делителей числа n
def sum_of_divisors(n):
    sum_of_divisors = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            sum_of_divisors += k
    return sum_of_divisors

# Подсчет суммы делителей всех натуральных чисел от 2 до max_number
lst = [0, 1]
for m in range(2, max_number + 1):
    lst.append(sum_of_divisors(m))

# Поиск дружественных чисел
for i in range(200, max_number + 1):
    for j in range(i + 1, max_number + 1):
        if i == lst[j] and j == lst[i]:
            print(i, j)
