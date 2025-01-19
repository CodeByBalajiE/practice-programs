# Find all prime numbers between two numbers
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find and print all prime numbers in the range
primes = [num for num in range(start, end + 1) if is_prime(num)]
print("Prime numbers in the range:", primes)
