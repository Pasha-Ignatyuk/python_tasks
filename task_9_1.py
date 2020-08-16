lst = ['We are surrounded in our daily lives with computers', 'computers are fast and have vast amounts of memory']
new_lst = [f'{i + 1} - {lst[i]}' for i in range(len(lst))]
print(new_lst)
