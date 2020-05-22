# Python Calculator
num1 = int(input ("Enter in first number: "))

operation = input('''
        Please type in the math operation you want to preform:

+ for addition
- for subtraction
/ for division
* for multiplication
''')

num2 = int(input ("Enter in second number: "))

if operation == '+':
    print('{} + {}'.format(num1, num2))
    print(num1 + num2)
    

if operation == '-':
    print('{} - {}'.format(num1, num2))
    print(num1 - num2)


if operation == '/':
    print('{} / {}'.format(num1, num2))
    print(num1 / num2)


if operation == '*':
    print('{} * {}'.format(num1, num2))
    print(num1 * num2)
