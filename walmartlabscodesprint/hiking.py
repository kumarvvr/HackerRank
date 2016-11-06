import math
n = int(input().strip())
frames = int(input().strip())
fac = math.factorial # Performance improvements
def C(n,r):
    return ((fac(n)//(fac(r)*fac(n-r))))
photos = 0
k = 1
while k<=n:
    photos += C(n,k)
    k+=1

print(abs(photos-frames))