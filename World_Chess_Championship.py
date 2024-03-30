# cook your dish here
T = int(input())

while T > 0:
    p = int(input())
    S = list(input())
    # Your code goes here
    T -= 1
    ch = 0 
    ca = 0 
    dr = 0 
    for i in S:
        if(i=='N'):
            ch += 1 
        elif(i=='C'):
            ca += 1 
        else:
            dr += 1 
    if(ca>ch):
        print(60*p)
    elif(ca<ch):
        print(40*p)
    else:
        print(55*p)
    
