def decorator(func):
    def wrapper(*args):
        new_sequence = tuple([args[-1 - i] for i in range(len(args))])
        result = func(*new_sequence)
        return result
    return wrapper


@decorator
def sequence(*args):
    print(*args)
    return args


sequence('f', 'g', 'h')
