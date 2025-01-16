def romanToInt(roman: str) -> int:
    # Dictionary to store Roman numeral values
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    
    total = 0
    for i in range(len(roman) - 1):
        # If the current numeral is smaller than the next one, subtract it
        if roman_map[roman[i]] < roman_map[roman[i + 1]]:
            total -= roman_map[roman[i]]
        else:
            total += roman_map[roman[i]]
    
    # Add the value of the last numeral
    total += roman_map[roman[-1]]
    
    return total
