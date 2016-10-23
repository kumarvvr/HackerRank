data = [int(x) for x in input().strip().split(' ')]

n = data[0]
k = data[1]
q = data[2]

data = [int(x) for x in input().strip().split(' ')]
dl = len(data)
ans = []

def getCIndex(input,length):
    while(input<0) : input += length
    return input%length


for i in range(q):
    query = int(input().strip())
    ans.append(data[getCIndex(query-k,dl)])

[print(a) for a in ans]