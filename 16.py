# Merge Intervals

def merge_intervals(a):
    a.sort(key=lambda x:x[0])
    l = []
    l.append(a[0])

    for i in a[1:]:
        last = l[-1]
        if last[1]>=i[0]:
            last[1] = max(last[1],i[1])
        else:
            l.append(i)

    print(l)            



a = [[1,3], [2, 4], [6, 8], [9, 10]]
merge_intervals(a)