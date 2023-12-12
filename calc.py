def summ(a, b):
    result = a + b
    return round(result, 2)


def sub(a, b):
    result = a - b
    return round(result, 2)


def mul(a, b):
    result = a * b
    return round(result, 2)


def div(a, b):
    if b == 0:
        return 'На ноль делить нельзя'
    else:
        result = a / b
    return round(result, 2)


def calculate(a, b, operation):
    result = None

    if operation == '+':
        result = summ(a, b)
    elif operation == '-':
        result = sub(a, b)
    elif operation == '/':
        result = div(a, b)
    elif operation == '*':
        result = mul(a, b)
    else:
        return ('Неизвестная операция')

    return result

