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


def getMaxCandies(students):

    def isPossibleValue(m):
        students_with_candies = [(pos, candy - m) for pos, candy in students]
        
        students_with_candies.sort()
        
        front = students_with_candies.copy()
        
        for i in range(len(front) - 1):
            if front[i][1] > 0:  
                distance = front[i+1][0] - front[i][0]
                transferable = max(0, front[i][1] - distance)
                
                front[i] = (front[i][0], front[i][1] - transferable)
                front[i+1] = (front[i+1][0], front[i+1][1] + transferable)
        
        back = students_with_candies.copy()
        
        for i in range(len(back) - 1, 0, -1):
            if back[i][1] > 0: 
                distance = back[i][0] - back[i-1][0]
                transferable = max(0, back[i][1] - distance)
                
                back[i] = (back[i][0], back[i][1] - transferable)
                back[i-1] = (back[i-1][0], back[i-1][1] + transferable)
        
        for i in range(len(students)):
            if front[i][1] < 0 and back[i][1] < 0:
                return False
        
        return True
    
    low = 0
    high = max(candy for _, candy in students)
    
    while low <= high:
        mid = (low + high) // 2
        if isPossibleValue(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return high 

def main():
    n = inp()
    students = []
    
    for _ in range(n):
        coordinate, candy = inlt()
        students.append((coordinate, candy))
    
    result = getMaxCandies(students)
    print(result)

if __name__ == "__main__":
    main()





# def trial(n, coords, candies):
#     diff = sum([coords[i]-coords[i-1] for i in range(1,n)])
#     print("Difference: ", diff)

#     total_candies = sum(candies)
#     remaining_candies = total_candies-(abs(diff))
#     print("Remaining Candies: ", remaining_candies)

#     return remaining_candies/n

# if __name__ == '__main__':
    
#     n = inp()
#     coords = []
#     candies = []
#     for _ in range(n):
#         (coord, candy) = inlt()
#         coords.append(coord)
#         candies.append(candy)

#     print("OUTPUT")
#     print("n: ",n)
#     print("Coordinates: ", coords)
#     print("Candies: ",candies)
#     print(trial(n, coords, candies))