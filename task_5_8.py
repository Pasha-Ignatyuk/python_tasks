"""В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы. [02-7.2-HL08]"""
string = 'Sequences: strings, lists, and tuples'
print(string)
lst = string.split()
print(lst)
lst_2 = lst[::-1]
print(lst_2)
string_2 = str(" ".join(lst_2))
print(string_2)
