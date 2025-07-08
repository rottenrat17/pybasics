#less go
#python calculator - stage 3
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

def get_number(text):
    while True:
        try :
            return float(input(text))
        except ValueError:
            print('Invalid Input')

def get_operator():
        valid_operators = ['+','-','*','/']
        while True:
            op = input('Please select an operator (+, - ,*, / ): ')
            if op in valid_operators:
                return op
            else :
                print('Invalid Operator, Please select a valid operator.')

def main():
    print('Welcome to Python Calculator')
    while True:
        num1 = get_number('Enter first number: ')
        operator = get_operator()
        num2 = get_number('Enter second number: ')

        try :
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = sub(num1, num2)
            elif operator == '*':
                result = mul(num1, num2)
            elif operator == '/':
                result = div(num1, num2)

            print(f"Result = {result}")
        except ZeroDivisionError:
            print('You cannot divide by zero')

        choice = input('Would you like to continue? (y/n): ').lower()
        if choice == 'n':
            print('Goodbye')
            break


if __name__ == '__main__':
    main()