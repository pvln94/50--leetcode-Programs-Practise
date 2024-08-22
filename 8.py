# Longest Common Prefix
def LCP(a):
    n = len(a)
    if n==0:
        return ""
    elif n==1:
        return a[0]
    else:
        a.sort()
        i = min(len(a[0]),len(a[-1]))
        j = 0

        while(j<i and a[0][j]==a[-1][j]):
            j+=1

        p = a[0][0:j]

        return p

if __name__ == "__main__" :
    a = ["ammammamma","ammamma","amma"]    
    print(LCP(a))

