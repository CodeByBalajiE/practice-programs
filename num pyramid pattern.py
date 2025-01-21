# Function to print a number pyramid pattern
def print_number_pyramid(n):
    for i in range(1, n + 1):  # Loop for each row
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end=" ")

        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()  # Move to the next line after each row

# Example Usage
n = 5  # Number of rows
print_number_pyramid(n)
