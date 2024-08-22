# Maximum Subarray
# Note: here list should be sorted only

def max_sum(a,l,h):
    def sum_middle(a,l,m,h):

        sm = 0
        left_sum = -1000
        for i in range(m,l-1,-1):
            sm = sm + a[i]

        if left_sum < sm:
            left_sum = sm

        sm = 0
        right_sum = -1000
        for i in range(m,h+1):
            sm = sm + a[i]

        if right_sum < sm:
            right_sum = sm    

        return max(left_sum+right_sum-a[m],left_sum,right_sum)    



    if a[l]>a[h]:
        return -1000
    elif a[l]==a[h]:
        return a[l]
    else:
        m= (l+h) // 2
        return max(max_sum(a,l,m),
                   max_sum(a,m+1,h),
                   sum_middle(a,l,m,h))



a = [1,2,3,4,5,6]
n=len(a)

res = max_sum(a,0,n-1)
print(res)