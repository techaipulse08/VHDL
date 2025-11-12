# Program to calculate Fibonacci numbers and count recursive steps

# Global variable to count steps
step_count = 0

def fibonacci(n):
    global step_count
    step_count += 1   # Count each function call
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main program
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("\nFibonacci Series:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print("\n\nTotal Recursive Steps:", step_count)
