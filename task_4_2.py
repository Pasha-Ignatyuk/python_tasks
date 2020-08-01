lst = [1, 2, 3, 4, 5]
sum_for = 0 # количество четных чисел для цикла с for
sum_while = 0 # количество четных чисел для цикла с while
for i in lst:
    remainder = float(i % 2)
    if remainder > 0.0:
        continue
    else:
        sum_for += 1
print(sum_for)

lenght = int(len(lst))
temporary = 0  # временная переменная для определения элемента исходного
# листа для цикла с while

while lenght > 0:
    item = lst[0 + temporary]
    remainder = float(item % 2)
    if remainder == 0.0:
        sum_while += 1
        temporary += 1
        lenght = lenght - 1
    else:
        temporary += 1
        lenght = lenght - 1

print(sum_while)