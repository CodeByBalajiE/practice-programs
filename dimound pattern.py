# Program to print a diamond pattern
rows = int(input("Enter the number of rows: "))

# Upper part of the diamond
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
