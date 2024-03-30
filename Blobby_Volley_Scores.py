t = int(input())
while t > 0:
    n = int(input())
    s = list(input())
    # Your code goes here
    t -= 1
    server_A = 1
    server_B = 0
    point_A = 0
    point_B = 0
    for i in range(n):
        if(s[i]=='A' and server_A == 1):
            point_A += 1
        elif(s[i]=='A' and server_A==0):
            server_A = 1
            server_B = 0
        elif(s[i]=='B' and server_B==0):
            server_B = 1
            server_A = 0
        elif(s[i]=='B' and server_B==1):
            point_B += 1
    print(point_A,point_B)
    
