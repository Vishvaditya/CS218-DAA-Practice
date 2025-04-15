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



def getMaxTrios(n, m, males, females):

    max_trios = 0
    j = 0
    
    for i in range(n):
        if j+1>=m:
            break
        elif females[j]<males[i] and females[j+1]<males[i]:
            max_trios+=1
            j+=2
            continue
        else:
            continue

    return max_trios


def main():

    n, m = inlt()
    male_heights = inlt()
    female_heights = inlt()
    male_heights.sort()
    female_heights.sort()
    print(getMaxTrios(n, m, male_heights, female_heights))
    


if __name__ == '__main__':
    main()