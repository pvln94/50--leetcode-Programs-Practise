# Find the duplicate number
a = [1, 6, 5, 2, 3, 3, 2]

l = []
for i in a:
    if a.count(i) > 1:
        l.append(i)


s = set(l)
print(s)