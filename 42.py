# Valid perfect square

import math

def check(n):
    r = int(math.sqrt(n))

    return (r*r == n)

n = 2400
r = check(n)
if(r):
    print("Yes")
else:
    print("No")