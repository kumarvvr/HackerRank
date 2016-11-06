import gcd from fractions

def lcm2(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def lcm(l):
    lcmSoFar = 1
    for k in l:   # loop should iterate m times
        lcmSoFar = lcm2(lcmSoFar, int(k))
    return lcmSoFar


(n,m) = [int(a) for a in input().strip().split(' ')]

A = [int(a) for a in input().strip().split(' ')]

B = [int(a) for a in input().strip().split(' ')]

alcm = lcm(A)

bmin = min(B)

ans=[]

for i in range(bmin-alcm+1):
    #Iterate until least number is reached.
    allfac = True
    for b in B:
        #Iterate through all elements
        if(b % alcm != 0):
            #Non factor found
            allfac = False
            break
    if(allfac): ans.append(alcm)
    alcm+=1

print(len(ans))
