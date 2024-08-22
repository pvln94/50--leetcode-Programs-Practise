# 4. Reverse Integer

l = [1,2,3,4]
print(l[::-1])

# or

l.reverse()
print(l)

#or 

def reverse_list(l):
    reversed_list = []
    for item in l:
        reversed_list.insert(0, item)
    return reversed_list

# Example usage
l = [1, 2, 3, 4]
reversed_l = reverse_list(l)
print(reversed_l)  # Output: [4, 3, 2, 1]
