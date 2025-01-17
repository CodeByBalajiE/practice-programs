# Program to print an inverted star pyramid
rows = int(input("Enter the number of rows: "))  # Number of rows for the pyramid

for i in range(rows, 0, -1):  # Loop through rows in reverse
    print(" " * (rows - i), end="")  # Print spaces for alignment
    print("* " * i)  # Print stars with spaces
