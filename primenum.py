# Program------prime number
def is_prime(number):
    # not prime
    if number < 2:
        return False

    # Check 1 and itself
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Not prime 
    return True  # Prime 
num = int(input("enter number"))
if is_prime(num):
    print("it is prime)
else:
    print("it is not prime")
