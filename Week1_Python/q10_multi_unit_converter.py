# Multi-Unit Converter System
# Converts temperature and length units
def convert_temp(value, from_unit, to_unit):
    try:
        if from_unit == 'C':
            if to_unit == 'F':
                return value * 9/5 + 32
            elif to_unit == 'K':
                return value + 273.15
        elif from_unit == 'F':
            if to_unit == 'C':
                return (value - 32) * 5/9
            elif to_unit == 'K':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'K':
            if to_unit == 'C':
                return value - 273.15
            elif to_unit == 'F':
                return (value - 273.15) * 9/5 + 32
        return value  # Same unit
    except:
        return None

def convert_length(value, from_unit, to_unit):
    try:
        units = {'m': 1, 'ft': 3.28084, 'in': 39.3701, 'km': 0.001, 'mi': 0.000621371}
        return value / units[from_unit] * units[to_unit]
    except:
        return None

# Menu-driven interface
def converter():
    while True:
        print("\n1. Temperature\n2. Length\n3. Exit")
        choice = input("Choose conversion type (1-3): ")
        
        if choice == '3':
            break
        elif choice in ['1', '2']:
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit: ").upper()
            to_unit = input("Enter to unit: ").upper()
            
            if choice == '1':
                result = convert_temp(value, from_unit, to_unit)
                units = ['C', 'F', 'K']
            else:
                result = convert_length(value, from_unit, to_unit)
                units = ['m', 'ft', 'in', 'km', 'mi']
            
            if result is None or from_unit not in units or to_unit not in units:
                print("Error: Invalid unit or input.")
            else:
                print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            print("Invalid choice.")

# Run the converter
if __name__ == "__main__":
    converter()