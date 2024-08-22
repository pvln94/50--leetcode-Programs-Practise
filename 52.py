# Write a program to print all the sub-sequences of a string in ascending order.
from itertools import combinations

def all_subsequences(s):
    subsequences = []
    
    # Generate all possible non-empty sub-sequences
    for length in range(1, len(s) + 1):
        for combo in combinations(s, length):
            subsequences.append(''.join(combo))
    
    # Sort the sub-sequences in ascending order
    subsequences.sort()
    
    return subsequences

# Example usage
s = "abc"
subsequences = all_subsequences(s)
print("Sub-sequences in ascending order:")
for subsequence in subsequences:
    print(subsequence)
