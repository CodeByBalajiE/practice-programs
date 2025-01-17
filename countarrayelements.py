# Program to count occurrences of an element in an array
arr = [2, 4, 2, 5, 2, 8, 4]  # Example array
target = int(input("Enter the element to count: "))  # Element to search for
count = 0

for num in arr:  # Loop through the array
    if num == target:  # Check if the element matches the target
        count += 1

print(f"{target} occurs {count} time(s) in the array.")
