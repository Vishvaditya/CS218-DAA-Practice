# import sys
# input = sys.stdin.readline

# def inp():
#     return(int(input()))
# def inlt():
#     return(list(map(int,input().split())))
# def insr():
#     s = input()
#     return(list(s[:len(s) - 1]))
# def invr():
#     return(map(int,input().split()))

# n = inp()
# arr = inlt()

n = 8
arr = [1,2,2,4,5,6,7,8] [1,1,3,4,5,6,7,8]

diff = 0

out = None

if arr[1]-arr[0] == arr[2]-arr[1]:
    actual_diff = arr[2]-arr[1]
elif arr[4]-arr[3] == arr[3]-arr[2]:
    actual_diff = arr[4]-arr[3]
else:
    actual_diff = arr[1]-arr[0]


for i in range(1, n):
    diff = arr[i] - arr[i-1]
    if diff!=actual_diff:
        out = i 
        break 

print(out) 
    




