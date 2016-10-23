import math

def lcm(x,y):
    return int((x*y)/(math.gcd(x,y)))

def nlcm(l):
    # l is a list of numbers.
    d = l[:]     # Make a copy of the input list
    lth = len(d)
    while(lth>1):
        x = d[-2:]
        d = d[0:-2]
        d.append(lcm(x[0],x[1]))
        lth -= 1
    return d
ans = []
t = int(input().strip())
for i in range(t):
    # Get the first line, extract n and k
    nk = [int(x) for x in input().strip().split(' ')]
    lst = [int(a) for a in input().strip().split(' ')]
    n = nk[0]
    k = nk[1]
    ans.append('YES') if (nlcm(lst))[0]%k == 0 else ans.append('NO')

[print(a) for a in ans]
