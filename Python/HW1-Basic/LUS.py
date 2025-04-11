import sys
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


def divideArray(arr, x):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
    
    return start

def getIncSequence(n, arr):
    ls = [0] * n
    temp_ls = []
    for i in range(n):
        pos = divideArray(temp_ls, arr[i])
        if pos == len(temp_ls):
            temp_ls.append(arr[i])
        else:
            temp_ls[pos] = arr[i]
        ls[i] = pos + 1
    return ls

def getLUS(n, arr):
    if not arr:
        return 0
    inc_seq = getIncSequence(n, arr)
    dec_seq = getIncSequence(n, arr[::-1])[::-1]
    return max(inc_seq[i] + dec_seq[i] - 1 for i in range(len(arr)))



if __name__ == "__main__":
    n = inp()
    arr = inlt()
    
    print(getLUS(n, arr))