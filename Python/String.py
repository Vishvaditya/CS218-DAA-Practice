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


def generateString(k):
    out_string = None
    if k==1:
        out_string = "ABC"
        return out_string
    else:
        out_string = "A"+generateString(k-1)+"B"+generateString(k-1)+"C"

    return out_string

def ABCStrings(string, l, r):
    return string[l:r]

def main(k, l, r):
    string = generateString(k)
    output = ABCStrings(string, l-1, r)
    # print(string)
    print(output)


if __name__=='__main__':
    t = inp()
    for i in range(t):
        inp_ls = inlt()
        k = inp_ls[0]
        l = inp_ls[1]
        r = inp_ls[2]
        main(k,l,r)

