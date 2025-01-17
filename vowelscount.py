# Program to count vowels in a string
text = input("Enter a string: ")  # Input string from the user
vowels = "aeiouAEIOU"  # List of vowels
count = 0

for char in text:  # Loop through each character in the string
    if char in vowels:  # Check if the character is a vowel
        count += 1

print(f"Number of vowels in the string: {count}")
