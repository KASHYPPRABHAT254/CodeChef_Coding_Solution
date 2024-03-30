t = int(input())
def decrement(i):
    s[i]=0
    if(-i>=len(s)):
        s.insert(0,1)
        return -1
    if(s[i-1]<9):
        s[i-1] = s[i-1]+1
        return -1
    else:
        decrement(i-1)
while t > 0:
    s = list(map(int,input()))
    t -= 1
    i = -1
    if(s[i]<9):
        s[i] = s[i]+1
    else:
        decrement(i)
    for j in s:
        print(j,end='')
    print('')
