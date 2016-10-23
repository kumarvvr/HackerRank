def completeHamming(s):
    a = ''
    for c in s:
        if c != 'a':
            a = a+'a'
        else:
            a=a+'b'
    return a

def convertHamming(s,k):
    if k == 0:
        # No changes to be done.
        return s
    if(len(s) == k):
        # All characters have to be changed
        return completeHamming(s)
    else:
        # Only first char has to be checked and changed.
        if s[0] != 'a':
            return('a'+convertHamming(s[1:],k-1)) # Do the conversion
        else:
            return('a'+ convertHamming(s[1:],k)) # No conversion done

t = int(input().strip())
ans = []
for i in range(t):
    inp = input().strip().split(' ')
    ans.append(convertHamming(inp[0],int(inp[1])))

[print(a) for a in ans]