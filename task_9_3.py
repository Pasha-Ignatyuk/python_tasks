lst = [2, 5, 7, 8, 9, 3]


def decorator(func):
    def wrapper(lst):
        new_list = [el for el in lst if el % 2 != 0]
        result = func(new_list)
        return result

    return wrapper


@decorator
def numlist(lst):
    print(lst)
    return lst


numlist(lst)
