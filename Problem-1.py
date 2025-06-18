# Problem-1.py

class Calculator:
    def calculate(self, a: float, b: float, operation: str):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            return a / b if b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

# Example
calc = Calculator()
print(calc.calculate(50, 5, 'add'))
print(calc.calculate(150, 30, 'divide'))            

# OUTPUT: 55 , 5.0
