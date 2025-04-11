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


def getSwaps(n, arr):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in range(n):
        if arr[i]==1:
            count_1+=1
        elif arr[i]==2:
            count_2+=1
        elif arr[i]==3:
            count_3+=1

    wrong_1_2 = wrong_1_3 = 0
    for i in range(count_1):
        if arr[i]==1:
            continue 
        elif arr[i]==2:
            wrong_1_2 += 1
        else:
            wrong_1_3 += 1

    wrong_2_1 = wrong_2_3 = 0
    for i in range(count_1, count_1+count_2):
        if arr[i]==2:
            continue 
        elif arr[i]==1:
            wrong_2_1 += 1
        else:
            wrong_2_3 += 1

    wrong_3_1 = wrong_3_2 = 0
    for i in range(count_1+count_2, n):
        if arr[i]==3:
            continue 
        elif arr[i]==1:
            wrong_3_1 += 1
        else:
            wrong_3_2 += 1

    swaps_1_2 = min(wrong_1_2, wrong_2_1)
    swaps_1_3 = min(wrong_1_3, wrong_3_1)
    swaps_2_3 = min(wrong_2_3, wrong_3_2)

    num_swaps = swaps_1_2+swaps_1_3+swaps_2_3

    
    indirect_swaps = 2*((wrong_1_2+wrong_1_3+wrong_2_1+wrong_2_3+wrong_3_1+wrong_3_2)-2*num_swaps)//3


    return num_swaps+indirect_swaps
    


if __name__ == '__main__':
    n = inp()
    arr = []
 
    # print(n)
    for i in range(n):
        arr.append(inp())

    print(getSwaps(n,arr))