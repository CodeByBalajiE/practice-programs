# Input an array and find the first repeating element
arr = [10, 5, 3, 4, 3, 5, 6]  # Example array
seen = set()
first_repeating = None

# Loop through the array and track seen elements
for num in arr:
    if num in seen:
        first_repeating = num
        break
    seen.add(num)

if first_repeating:
    print(f"The first repeating element is: {first_repeating}")
else:
    print("No repeating elements found.")
