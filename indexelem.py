# Program to find the index of an element in a list
numbers = [10, 20, 30, 40, 50]  # Example list
target = int(input("Enter the number to find: "))  # Input target number

found = False
for i in range(len(numbers)):  # Loop through the list using indices
    if numbers[i] == target:  # Check if the current element matches the target
        print(f"{target} found at index {i}")
        found = True
        break

if not found:
    print(f"{target} is not in the list.")
