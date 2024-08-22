# Sort colors

# Python Program to sort an array of 0s, 1s and 2s

# Function to sort an array of 0s, 1s and 2s
def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0

    # Count 0s, 1s and 2s
    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
    # Place all the 0s
    for i in range(c0):
        arr[idx] = 0
        idx += 1

    # Place all the 1s
    for i in range(c1):
        arr[idx] = 1
        idx += 1

    # Place all the 2s
    for i in range(c2):
        arr[idx] = 2
        idx += 1


# Sample Input
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012(arr)

for x in arr:
  print(x, end = " ")
