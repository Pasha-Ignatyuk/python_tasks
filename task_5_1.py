"""Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без перезагрузки
программа (т.е. построить бесконечный цикл). В качестве символа прекращения
вычислений принять ‘0’ (т.е. sign='0')"""
while True:
    a = input('Введите первый операнд или введите слово "stop", чтобы выйти из программы')
    if a == "stop":
        break
    else:
        try:
            operand_1 = int(a)
        except Exception:
            print('введите числовое значение')
        operator = input('Введите математический оператор: + – / или *')
        operand_2 = int(input('Введите второй операнд'))
        if operator == "+":
            outcome = operand_1 + operand_2
            print(outcome)
        if operator == "-":
            outcome = operand_1 - operand_2
            print(outcome)
        if operator == "/":
            try:
                outcome = operand_1 / operand_2
                print(outcome)
            except ZeroDivisionError as err:
                print(f'Делить на ноль нельзя - {err}!!!')
        if operator == "*":
            outcome = operand_1 * operand_2
            print(outcome)
        if not(operator == '+') and not(operator == '-') and not(operator == '/') and not(operator == '*'):
            print('введите только один из следующих математических операторов: + – / или *')
