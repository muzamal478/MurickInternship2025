# Circle Properties Calculator
# Calculates area and circumference of a circle with input validation
import math

def circle_properties():
    try:
        # Get radius from user
        radius = float(input("Enter radius: "))
        if radius <= 0:
            print("Error: Radius must be positive")
            return
        
        # Calculate area and circumference
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        
        # Format output to 2 decimal places
        print(f"Area: {area:.2f}")
        print(f"Circumference: {circumference:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter a number.")

# Run the calculator
if __name__ == "__main__":
    circle_properties()