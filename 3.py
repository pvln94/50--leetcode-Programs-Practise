# Largest Substring without repeating characters

a="aabcdefffdd"
b = list(a)

n = len(b)
Substring = []
max_length = 0

for i in range(n):
    l = []
    seen = set()
    for j in range(i,n):
        if b[j] in seen:
            break
        seen.add(b[j])
        l.append(b[j])
    if len(l) > max_length:
        max_length = len(l)      
        Substring = l

# print(Substring)
print("".join(Substring))