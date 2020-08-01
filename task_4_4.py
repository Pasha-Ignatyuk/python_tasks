lst = [1, 2, 3, 4, 5]

lst_2_1 = []  # для цикла с while
lst_2_2 = []  # для цикла с for

first_item = lst.pop(0)
length = len(lst)
temporary = 0

while length > 0:
    item = lst[temporary]
    lst_2_1.append(item)
    temporary += 1
    length -= 1
else:
    lst_2_1.append(first_item)
print(lst_2_1)

for i in lst:
    lst_2_2.append(i)
else:
    lst_2_2.append(first_item)
print(lst_2_2)
