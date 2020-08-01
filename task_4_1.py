lst = [1, 2, 3, 4]
lst_2_1 = []  # для цикла с while
lst_2_2 = []  # для цикла с for

lenght = int(len(lst))

temporary = 0  # временная переменная для определения элемента исходного
# листа для цикла с while

while lenght > 0:
    item = lst[0 + temporary]
    negative_item = item * -2
    lst_2_1.append(negative_item)
    temporary += 1
    lenght = lenght - 1
print(lst_2_1)

for i in lst:
    lst_2_2.append(i * -2)
print(lst_2_2)
