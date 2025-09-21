# Mathematical Sequence Generator
# Generates Fibonacci, prime, or perfect square sequences
import math

def fib(n):
    a, b = 0, 1
    seq = []
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq

def primes(limit):
    return [i for i in range(2, limit + 1) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

def perfect_squares(low, high):
    return [i ** 2 for i in range(int(low ** 0.5), int(high ** 0.5) + 1) if low <= i ** 2 <= high]

def fib_primes(n, limit):
    fib_seq = fib(n)
    prime_seq = primes(limit)
    return [x for x in fib_seq if x in prime_seq]

# Get user choice
try:
    choice = input("Choose sequence (fib/primes/squares/fib_primes): ").lower()
    if choice == "fib":
        n = int(input("Enter length: "))
        print(fib(n))
    elif choice == "primes":
        limit = int(input("Enter limit: "))
        print(primes(limit))
    elif choice == "squares":
        low, high = map(int, input("Enter range (low high): ").split())
        print(perfect_squares(low, high))
    elif choice == "fib_primes":
        n = int(input("Enter Fibonacci length: "))
        limit = int(input("Enter prime limit: "))
        print(fib_primes(n, limit))
    else:
        print("Invalid choice")
except ValueError:
    print("Error: Invalid input.")