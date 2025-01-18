# Program to find the GCD of two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:  # Use the Euclidean algorithm
    a, b = b, a % b  # Update 'a' and 'b'

print(f"The GCD of the two numbers is {a}.")
