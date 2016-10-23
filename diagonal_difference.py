n = int(input().strip())

mat = []

# Gather data into a nested list.
for i in range(n):
    mat.append([int(x) for x in input().strip().split(' ')])

cr=0
cl=-1
sum = 0
# Loop through the diagonals and sum them up
for row in mat:
    sum = sum+(row[cr] - row[cl])
    cr += 1
    cl -= 1
print(abs(sum))