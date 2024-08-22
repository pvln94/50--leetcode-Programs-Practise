# Reverse vowels in a string
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)  # Convert string to list to modify characters
    i, j = 0, len(s) - 1

    while i < j:
        if s_list[i] not in vowels:
            i += 1
        elif s_list[j] not in vowels:
            j -= 1
        else:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

    return ''.join(s_list)  # Convert list back to string

# Example usage
input_str = "hello"
reversed_vowels_str = reverse_vowels(input_str)
print(reversed_vowels_str)  # Output will be "holle"

input_str = "leetcode"
reversed_vowels_str = reverse_vowels(input_str)
print(reversed_vowels_str)  # Output will be "leotcede"
