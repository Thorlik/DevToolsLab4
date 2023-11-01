import calc

while True:
    a = float(input('Введите первое число: '))
    operation = input('Выберите операцию: ')
    b = float(input('Введите второе число: '))

    if operation == 'exit':
        break
    result = calc.calculate(a, b, operation)

    print(f'Результат вычислений: {result}')