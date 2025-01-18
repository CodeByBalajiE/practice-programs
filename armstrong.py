# Program to check if a number is an Armstrong number
num = int(input("Enter a number: "))  # Input number
num_str = str(num)
n = len(num_str)  # Number of digits
sum_of_powers = sum(int(digit) ** n for digit in num_str)  # Sum of digits raised to the power of n

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
