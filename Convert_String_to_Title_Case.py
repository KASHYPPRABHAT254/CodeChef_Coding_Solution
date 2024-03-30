# cook your dish here
T = int(input())

while T > 0:
    S = list(map(str,input().split(' ')))
    # Your code goes here
    T -= 1
    for i in S:
        if(i.isupper()):
            print(i,end=' ')
        else:
            i = i.lower()
            j =list(i)
            print(j[0].upper(),end='')
            for k in range(1,len(j)):
                print(j[k],end='')
            print(' ',end='')
    print('')
            
            
            
