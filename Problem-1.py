class Cal:
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
ans = Cal()
print(ans.calculate(50, 5, 'add'))
print(ans.calculate(150, 30, 'divide'))            

# OUTPUT: 55 , 5.0
