# cook your dish here
T = int(input())

while T > 0:
    N = int(input())
    S = list(input())
    # Your code goes here
    T -= 1
    count = 0
    for i in range(N-1):
        if(S[i]==S[i+1]):
            count += 1
    print(count)
    
            
