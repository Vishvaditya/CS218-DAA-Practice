import sys
import time

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


# def generateString(k):
#     out_string = None
#     if k==1:
#         out_string = "ABC"
#         return out_string
#     else:
#         out_string = "A"+generateString(k-1)+"B"+generateString(k-1)+"C"

#     return out_string

# def ABCStrings(string, l, r):
#     return string[l:r]

# def main(t, k, l, r):
#     for i in range(1,t):
#         print(generateString(i))
#         print(len(generateString(i)))
#     return
#     string = generateString(k)
#     output = ABCStrings(string, l-1, r)
#     # print(string)
#     print(output)


# if __name__=='__main__':
#     t = inp()
#     t = 4
#     main(t,1,1,1)
#     for i in range(t):
#         inp_ls = [1,2,3]#inlt()
#         k = inp_ls[0]
#         l = inp_ls[1]
#         r = inp_ls[2]
#         main(k,l,r)

K_MAX = 50
LENGTHS = []
LENGTHS.append(3)
for i in range(1, K_MAX):
    LENGTHS.append(2*(LENGTHS[i-1])+3)

# print(LENGTHS)

def getCharacter(k, pos):
    # Base Case
    # print('pos: ', pos)
    curr_k = k
    curr_pos = pos

    while curr_k > 0:
        # print('K: ', curr_k, "POS: ", curr_pos)

        mid_b= 1 + LENGTHS[curr_k - 1]

        if curr_pos == 0:
            # print('----CKP 1----')
            return 'A' 

        if curr_pos < mid_b:
            # print('----CKP 2----')
            curr_k -= 1
            curr_pos -= 1 
            continue 

        if curr_pos == mid_b:
            # print('----CKP 3----')
            return 'B' 


        if curr_pos < LENGTHS[curr_k]-1:
            #  print('----CKP 4----')

             curr_pos -= mid_b+1
             curr_k -= 1
             continue 


        # print('----CKP 5----')
        return 'C' 


    # print('----CKP 6----')
    return "ABC"[curr_pos]
    
def main(k, l, r):
    out_string = ""
    for i in range(l-1, r):
        out_char = getCharacter(k-1, i)
        # print(i, out_char)
        out_string+=out_char
    return out_string

if __name__ == '__main__':
    t = inp()
    test_cases = []
    max_k = 0
    out_ls = []
    for _ in range(t):
        k, l, r = inlt()
        start_time = time.time()
        result_ls = []
        for i in range(l-1, r):
            out_char = getCharacter(k-1, i)
            result_ls.append(out_char)
        
        out_ls.append("".join(result_ls))

    sys.stdout.write("\n".join(out_ls) + "\n")
    print("--- %s seconds ---" % (time.time() - start_time))