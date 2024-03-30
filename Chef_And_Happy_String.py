t = int(input())

while t > 0:
    s = list(input())
    # Your code goes here
    t -= 1
    f = 0
    for i in range(len(s)-2):
        if(s[i] in ['a','e','i','o','u'] and s[i+1] in ['a','e','i','o','u'] and s[i+2] in ['a','e','i','o','u'] ):
            f = 1
            break
    if(f==1):
        print("Happy")
    else:
        print("Sad")
    
