def summ(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    if b == 0:
        return 'На ноль делить нельзя'
    else:
        result = a / b
    return result


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
        print('Неизвестная операция')

    return result

