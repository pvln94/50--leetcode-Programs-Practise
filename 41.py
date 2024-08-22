# First unique character in a string

def firstUniqChar(s):
    n = len(s)

    # Step 1: Iterate over each character in the string
    for i in range(n):
        found = True

        # Step 2: Check if the character repeats in the rest of the string
        for j in range(n):
            if i != j and s[i] == s[j]:
                found = False
                break

        # Step 3: If character does not repeat, return its index
        if found:
            return i

    # Step 4: If no such character is found, return -1
    return -1


# Driver code
s = "geeksforgeeks"
print(firstUniqChar(s))
