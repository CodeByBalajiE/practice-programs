# Input a string and find the longest palindromic substring
text = input("Enter a string: ")

def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

longest_palindrome = ""

# Check all substrings for palindrome property
for i in range(len(text)):
    for j in range(i, len(text)):
        substring = text[i:j+1]
        if is_palindrome(substring) and len(substring) > len(longest_palindrome):
            longest_palindrome = substring  # Update longest palindrome

print(f"The longest palindromic substring is: {longest_palindrome}")
