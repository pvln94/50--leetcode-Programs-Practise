# Decode String
def decode_string(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = ""
            while stack and stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()  # Remove the '['
            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)
    return ''.join(stack)

# Example usage
input_str = "3[a]2[bc]"
decoded_str = decode_string(input_str)
print(decoded_str)  # Output will be "aaabcbc"

input_str = "3[a2[c]]"
decoded_str = decode_string(input_str)
print(decoded_str)  # Output will be "accaccacc"

input_str = "2[abc]3[cd]ef"
decoded_str = decode_string(input_str)
print(decoded_str)  # Output will be "abcabccdcdcdef"
