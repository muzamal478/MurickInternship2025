# Smart Calculator
# Takes two numbers and an operator, handles division by zero, and formats output
def smart_calculator():
    try:
        # Get input from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /, **, %): ")
        
        # Perform calculation based on operator
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ValueError("Division by zero is not allowed")
            result = num1 / num2
        elif op == '**':
            result = num1 ** num2
        elif op == '%':
            result = num1 % num2
        else:
            raise ValueError("Invalid operator")
        
        # Format output to match requirement (e.g., 5.0 + 3.0 = 8.0)
        print(f"{num1:.1f} {op} {num2:.1f} = {result:.1f}")
    except ValueError as e:
        print(f"Error: {e}")

# Run the calculator
if __name__ == "__main__":
    smart_calculator()