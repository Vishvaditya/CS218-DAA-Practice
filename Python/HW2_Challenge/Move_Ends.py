import sys
# from collections import deque
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def getMinOperations(n, arr):
    pos_dict = {}
    for i in range(n):
        pos_dict[arr[i]] = i

    length = 1
    ss_len = 1

    for i in range(2, n+1):
        if pos_dict[i]>pos_dict[i-1]:
            length +=1
        else:
            length = 1
        
        ss_len = max(ss_len, length)

    return n-ss_len


def main():
    t = inp()

    for _ in range(t):
        n = inp()
        arr = inlt()
        print(getMinOperations(n, arr))


if __name__ == '__main__':
    main()