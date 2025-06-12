def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Generate the first 'n' numbers
    for _ in range(n):
        yield a          # Output the current Fibonacci number
        a, b = b, a + b  # Update to the next pair of numbers

# Example usage:
n = 10
print(f"First {n} Fibonacci numbers:")
for num in fibonacci(n):
    print(num, end=" ")