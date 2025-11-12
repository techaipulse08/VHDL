# Fibonacci series with step count
steps = 0

def fibonacci(n):
    global steps
    steps += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
print("\nTotal steps:", steps)



# TIME COMPLEXITY:
# Recursive approach: O(2ⁿ)