t = input().strip()
time = t[2:-2]
h=(t[0:2])
if(t[-2:] == 'PM'):
    
    h =str(int(h)+12)
    if h ==  '24' : h = '12' # Implicit conversion

else:
    if (h == '12'):
        h = '00'
h = str(h)+str(time)
print(h)
