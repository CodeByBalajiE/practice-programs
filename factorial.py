#factorial number
def factorial(n):
    # Start with 1 
    result = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        result = result * i  # Multiply each number with result
    return result
num = int(input("Enter number"))
# Handle negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print("The factorial of", num, "is", fact)
