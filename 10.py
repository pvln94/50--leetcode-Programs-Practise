# Roman to Integer
def roman_to_int(s):
    # Define mappings of Roman numerals to integers
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    
    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string
    for char in s:
        # Get the integer value of the current Roman numeral
        value = roman_to_int_map[char]
        
        # If the previous value is smaller, subtract twice the previous value
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        
        # Update the previous value
        prev_value = value

    return total

# Example usage
roman_numeral = "MCMXCIV"
print(f"The integer value of Roman numeral '{roman_numeral}' is {roman_to_int(roman_numeral)}")  # Output: 1994
