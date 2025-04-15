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



def getHappyPeople(n, r, members):
    total_people = sum(members)
    total_seats = 2*r 

    max_happy = 0
    remaining_members = 0

    for i in range(n):
        max_happy += (members[i]//2)*2
        remaining_members += members[i]%2
        # print(f"remaining {i}: ", remaining_members)
    
    remaining_seats = total_seats-max_happy
    remaining_rows = remaining_seats//2
    # print("Max_happy: ", max_happy)
    # print('remaining_members: ', remaining_members)
    # print('remaining_seats: ', remaining_seats)
    # print('remaining_rows: ', remaining_rows)

    if remaining_seats==0:
        return max_happy

    # if remaining_rows%2!=0:
    #     print('WRoNG LOGIC')
    #     return 0
    
    if remaining_rows>=remaining_members:
        max_happy += remaining_members
        return max_happy
    
    else:
        max_happy += remaining_seats-remaining_members
        return max_happy


def main():
    t = inp()

    for _ in range(t):
        n, r = inlt()
        members = inlt()
        print(getHappyPeople(n, r, members))


if __name__ == '__main__':
    main()