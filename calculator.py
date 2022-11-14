what = input('Выберите операцию: +;-;/;*:**')

a = float(input('Ведите первое чилсо: '))
b = float(input('Введите второе число: '))

if what == '+':
    c = a + b
elif what == '-':
    c = a - b
elif what == '/':
    c = a / b
elif what == '*':
    c = a * b
elif what == '**':
    c = a ** b

print('Результат ' + str(c))
