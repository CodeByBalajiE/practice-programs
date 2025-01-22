# Count how many digits in number
number = 12345  # The number to check
count = 0  # Start with no digits counted

# Use loop to count digits
while number > 0:
    number = number // 10  # Remove last digit
    count += 1  # Increas count

# Showing result
print("The number of digits is", count,)
