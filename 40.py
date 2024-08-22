# Top K frequent elements
a = [3, 1, 4, 4, 5, 2, 6, 1]
k = 2

# Convert the list to a set to remove duplicates
unique_elements = set(a)

# Initialize a counter
count = 0

# Iterate over the set and print the first k elements
for element in unique_elements:
    if count < k:
        print(element)
        count += 1
    else:
        break
