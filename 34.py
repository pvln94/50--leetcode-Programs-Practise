# Move Zeros

a = [1,2,0,4,3,0,5,0]
l=[]
for i in range(len(a)):
    if a[i] != 0:
        l.append(a[i])
n = len(a) - len(l)
l=l+[0]*n     
print(l)


