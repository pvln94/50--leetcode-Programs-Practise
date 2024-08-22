# Next permutation

def next_permutation(nums):
    # Find the first element from the right that is not in decreasing order
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # If such an element is found, find the smallest element from the right that is greater than it
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap the two elements
        nums[i], nums[j] = nums[j], nums[i]
    # Reverse the elements from i+1 to the end to get the next permutation
    nums[i + 1:] = reversed(nums[i + 1:])

nums = [2,4,1,7,5,0]
next_permutation(nums)
print(nums)
