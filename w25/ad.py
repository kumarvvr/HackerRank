s = input().strip()
t = input().strip()
k = int(input().strip())

ls = len(s)
lt = len(t)

ops = 0
if s == t:
    ops = ls*2 + 1
elif ls<lt:
    ops += lt-ls # These many operations are definitely required.
    idx = 0
    for i in range(ls):
        if(s[i] != t[i]):
           idx = i
           break # Come out of loop.
    if idx != 0:
        ops+= (ls-idx)*2
else:
    ops+= ls-lt # Even equal case is counted here.
    idx = 0
    for i in range(lt):
        if(s[i] != t[i]):
           idx = i
           break # Come out of loop.
    if idx != 0:
        ops+= (lt-idx)*2

print('Yes') if(ops==k) else print('No')