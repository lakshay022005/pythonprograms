class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return 'Error: division by zero'
        return self.a / self.b


def main():
    print('Simple OOP Calculator')
    try:
        x = float(input('Enter first number: '))
        y = float(input('Enter second number: '))
    except ValueError:
        print('Please enter valid numbers.')
        return

    calc = Calculator(x, y)

    print('Addition:', calc.add())
    print('Subtraction:', calc.subtract())
    print('Multiplication:', calc.multiply())
    print('Division:', calc.divide())


if __name__ == '__main__':
    main()
