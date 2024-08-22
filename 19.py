# Search a 2D Matrix

# we need to search element in a 2d matrix using linear search


# index starts from 0 to 2, matrix of size 3x3 (0,1,2)

def search(a,k):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == k:
                return [i,j]

    return [-1,-1]        

a = [[1,2,3],[4,5,6],[7,8,9]]
k = 6

res = search(a,k)
print(f"Element found at [{res[0]},{res[1]}]")


