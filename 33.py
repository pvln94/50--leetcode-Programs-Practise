# Missing Number

def missingnum(n,arr):
    hash = [0] * (n+1)

    for i in arr:
        hash[i] += 1

    for i in range(1,n+1):
        if hash[i]==0:
            return i
    return -1   

a = [1,2,3,5]
n=5
print(missingnum(n,a)) 

