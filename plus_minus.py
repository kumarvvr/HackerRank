n = int(input().strip())

p = 0
ng = 0
z = 0

for i in [int(x) for x in input().strip().split(' ')]:
    if i <0 : ng += 1
    elif i>0 : p += 1
    else : z += 1

print(format(p/n,".6f"))
print(format(ng/n,".6f"))
print(format(z/n,".6f"))