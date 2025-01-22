# Reverse digits of a number
num = 12345  
reversednum = 0  # Start with 0
while num > 0:
    digit = num % 10  # Get the last digit
    reversednum = reversednum * 10 + digit  # Add to reversed number
    num = num // 10  # Remove last digit
print("The reversed number is:", reversednum)
