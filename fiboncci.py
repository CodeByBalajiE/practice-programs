# FIBONACCI PROG
n = int(input("Enter the number of terms: "))

# Initialize first two terms 
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update terms for next iteration
