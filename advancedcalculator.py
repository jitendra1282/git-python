import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take square root of a negative number."

def logarithm(x, base=10):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error! Logarithm undefined for non-positive values."

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial not defined for negative numbers."
    else:
        return math.factorial(int(x))

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def advanced_calculator():
    print("Advanced Calculator")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (sqrt)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Factorial (fact)")
    
    while True:
        operation = input("\nEnter operation (or 'exit' to quit): ").lower()
        
        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if operation in ['+', '-', '*', '/', '^']:
            x = get_float_input("Enter first number: ")
            y = get_float_input("Enter second number: ")
            if operation == '+':
                print(f"{x} + {y} = {add(x, y)}")
            elif operation == '-':
                print(f"{x} - {y} = {subtract(x, y)}")
            elif operation == '*':
                print(f"{x} * {y} = {multiply(x, y)}")
            elif operation == '/':
                print(f"{x} / {y} = {divide(x, y)}")
            elif operation == '^':
                print(f"{x} ^ {y} = {power(x, y)}")
                
        elif operation == 'sqrt':
            x = get_float_input("Enter number: ")
            print(f"Square root of {x} = {square_root(x)}")
        
        elif operation == 'log':
            x = get_float_input("Enter number: ")
            base_input = input("Enter base (default 10): ")
            base = float(base_input) if base_input else 10
            print(f"Logarithm of {x} with base {base} = {logarithm(x, base)}")
        
        elif operation == 'sin':
            x = get_float_input("Enter angle in degrees: ")
            print(f"Sine of {x}° = {sine(x)}")
        
        elif operation == 'cos':
            x = get_float_input("Enter angle in degrees: ")
            print(f"Cosine of {x}° = {cosine(x)}")
        
        elif operation == 'tan':
            x = get_float_input("Enter angle in degrees: ")
            print(f"Tangent of {x}° = {tangent(x)}")
        
        elif operation == 'fact':
            x = get_float_input("Enter number: ")
            print(f"Factorial of {int(x)} = {factorial(x)}")
        
        else:
            print("Invalid operation. Please try again.")

# Run the calculator
