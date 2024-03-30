# Wordle
# Chef invented a modified wordle.
# There is a hidden word S and a guess word T, both of length 5.
# Chef defines a string M to determine the correctness of the guess word. For the ith index:
# If the guess at the ith index is correct, the ith character of M is G.
# If the guess at the ith index is wrong, the ith character of M is B.
# Given the hidden word S and guess T, determine string M.
# Output Format
# For each test case, print the value of string M.
# You may print each character of the string in uppercase or lowercase (for example, the strings 
# BgBgB,BgBgB,BGBGB,BGBGB,bgbGB,bgbGB and bgbgb,bgbgb will all be treated as identical).
# Constraints
# 1≤T≤1000
# 1≤T≤1000
# ∣S∣=∣T∣=5
# S,T contain uppercase english alphabets only.

# input

# 3
# ABCDE
# EDCBA
# ROUND
# RINGS
# START
# STUNT

# output

# BBGBB
# GBBBB
# GGBBG
# cook your dish here
T = int(input())

while T > 0:
    S = list(input())
    H = list(input())
    # Your code goes here
    T -= 1
    for i in range(len(S)):
        if(S[i]==H[i]):
            print('G',end='')
        else:
            print('B',end='')
    print('')
    
