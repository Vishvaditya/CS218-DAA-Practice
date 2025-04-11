a = [(1,2,3),
     (4,5,6),
     (7,8,9)]

# for i,j,k in a:
#     print(i, j, k)

print("ABC"[0])

def max_candies(students):
    # Binary search to find the maximum achievable value m
    def is_possible(m):
        # Create a copy of students with their positions and adjusted candies
        students_with_candies = [(pos, candy - m) for pos, candy in students]
        
        # Sort by position for easier processing
        students_with_candies.sort()
        
        # Forward pass (left to right)
        forward = students_with_candies.copy()
        
        for i in range(len(forward) - 1):
            if forward[i][1] > 0:  # If this student has excess
                # Calculate distance to next student
                distance = forward[i+1][0] - forward[i][0]
                # Maximum transferable amount after distance loss
                transferable = max(0, forward[i][1] - distance)
                
                forward[i] = (forward[i][0], forward[i][1] - transferable)
                forward[i+1] = (forward[i+1][0], forward[i+1][1] + transferable)
        
        # Backward pass (right to left)
        backward = students_with_candies.copy()
        
        for i in range(len(backward) - 1, 0, -1):
            if backward[i][1] > 0:  # If this student has excess
                # Calculate distance to previous student
                distance = backward[i][0] - backward[i-1][0]
                # Maximum transferable amount after distance loss
                transferable = max(0, backward[i][1] - distance)
                
                backward[i] = (backward[i][0], backward[i][1] - transferable)
                backward[i-1] = (backward[i-1][0], backward[i-1][1] + transferable)
        
        # For each position, take the better result of forward or backward
        for i in range(len(students)):
            if forward[i][1] < 0 and backward[i][1] < 0:
                return False
        
        return True
    
    # Binary search
    low = 0
    high = max(candy for _, candy in students)
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return high  # Return the maximum achievable value

def main():
    n = int(input())
    students = []
    
    for _ in range(n):
        position, candy = map(int, input().split())
        students.append((position, candy))
    
    result = max_candies(students)
    print(result)

if __name__ == "__main__":
    main()

