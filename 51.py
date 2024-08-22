# Write a program to find the sum of all sub-arrays of a given integer array.
def sum_of_subarrays(arr):
    total_sum = 0
    n = len(arr)
    
    for i in range(n):
        subarray_sum = 0
        for j in range(i, n):
            print(arr[j])
            subarray_sum += arr[j]
            total_sum += subarray_sum
    
    return total_sum

arr = [1, 2, 3]
print("Sum of all sub-arrays:", sum_of_subarrays(arr))
