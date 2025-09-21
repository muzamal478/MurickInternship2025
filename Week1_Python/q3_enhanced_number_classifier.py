# Enhanced Number Classifier
# Analyzes a number for sign, parity, perfect square, and power of 2
import math

def classify_number(n):
    # Determine sign
    sign = "positive" if n > 0 else "negative" if n < 0 else "zero"
    
    # Determine even/odd
    even_odd = "even" if n % 2 == 0 else "odd"
    
    # Check if perfect square
    perfect_square = "yes" if math.isqrt(n) ** 2 == n else "no"
    
    # Check if power of 2
    power_of_2 = "yes" if n > 0 and (n & (n - 1)) == 0 else "no"
    
    # Print results
    print(f"Sign: {sign}")
    print(f"Even/Odd: {even_odd}")
    print(f"Perfect Square: {perfect_square}")
    print(f"Power of 2: {power_of_2}")

# Get input and run classifier
try:
    n = int(input("Enter number: "))
    classify_number(n)
except ValueError:
    print("Error: Please enter an integer.")