#revers string
def reverse_string(text):
    reversedtext = ""  # Initialize empty string
    for char in text:
        reversed_text = char + reversedtext  # Add each character beginning
    return reversedtext
userinput = input("Enter a string to reverse: ")
result = reversestring(userinput)
print("The reversed string is:", result)
