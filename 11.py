# Merge 2 sorted lists

def merge(a,b):
    array = [0] * (len(a) + len(b))
    
    i,j,k = 0,0,0

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k+=1

    while i < len(a):
        array[k] = a[i]
        i+=1
        k+=1

    while j < len(b):
        array[k] = b[j]
        j+=1
        k+=1  

    return array

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == "__main__":
    a = [1,2,3,4]
    b=[5,6,7,8]
    
    array=merge(a,b)     

    printList(array)

               
