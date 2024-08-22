# Remove duplicates from sorted array

a = [1,2,3,4,5,1,2,3,4,6]
a.sort()
# result = set(a)
# print(result)

res = []
for i in a:
    if i not in res:
        res.append(i)

print(res)