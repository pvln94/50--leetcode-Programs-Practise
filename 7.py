# Container with most water

# Given n non-negative integers a_1, a_2, ..., a_n                  
# where each represents a point at coordinate (i, a_i).
# ‘ n ‘ vertical lines are drawn such that the two endpoints of line i is at (i, a_i) and (i, 0)                  . 
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.

def container(a,n):
    area = 0
    for i in range(0,n):
        for j in range(i+1,n):
            area = max(area,min(a[i],a[j])*(j-i))

    return area

a = [1,8,6,2,5,4,8,3,7]
n = len(a)

print(container(a,n))