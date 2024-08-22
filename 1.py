# 2 sum problem
# check if given value exits by summing any 2 numbers in array

def sum(l,v,n):
    for i in range(0,n-1):
        for j in range(i+1,n-1):
            if l[i] + l[j] == v:
                return 1
            return 0
            
        
if __name__ == "__main__":
    a = [1,2,3,4,5]
    v=3
    n = len(a)
    r = sum(a,v,n)
    if(r):
        print("There exist numbers whose sum is 3")
    else:
        print("Doesnot exist")

            