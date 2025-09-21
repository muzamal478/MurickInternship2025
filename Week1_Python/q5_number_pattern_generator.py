# Number Pattern Generator
# Prints numbers with custom replacements for multiples
def pattern_generator(start=1, end=100, div1=3, word1="Boom", div2=5, word2="Crash"):
    try:
        # Iterate through range
        for i in range(start, end + 1):
            if i % div1 == 0 and i % div2 == 0:
                print(word1 + word2)
            elif i % div1 == 0:
                print(word1)
            elif i % div2 == 0:
                print(word2)
            else:
                print(i)
    except Exception as e:
        print(f"Error: {e}")

# Get custom inputs
try:
    start = int(input("Enter start range (default 1): ") or 1)
    end = int(input("Enter end range (default 100): ") or 100)
    div1 = int(input("Enter first divisor (default 3): ") or 3)
    word1 = input("Enter first word (default Boom): ") or "Boom"
    div2 = int(input("Enter second divisor (default 5): ") or 5)
    word2 = input("Enter second word (default Crash): ") or "Crash"
    pattern_generator(start, end, div1, word1, div2, word2)
except ValueError:
    print("Error: Invalid input. Using defaults.")
    pattern_generator()