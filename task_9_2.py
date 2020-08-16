def Diction():
    dictionary = {}
    while (True):
        print('введите ключ или введите end для выхода из программы')
        enter_key = input()
        if enter_key == 'end':
            break
        print('введие значение ключа')
        enter_value = input()
        dictionary[enter_key] = enter_value
        new_dict = {key * 2: value for key, value in dictionary.items()}
    return new_dict


monitor = Diction()
print(monitor)
