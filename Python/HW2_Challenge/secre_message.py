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


# def getSecretMessage(grid, N, M, out_string):


#     def dfs(x, y, mask, curr_string):
#         nonlocal out_string

#         # Prune only if cur is strictly greater than the best prefix
#         if out_string is not None and curr_string > out_string[:len(curr_string)]:
#             return

#         # If we've reached bottom-right, see if we improve best
#         if x == N-1 and y == M-1:
#             if out_string is None or curr_string < out_string:
#                 out_string = curr_string
#             return

#         # Collect unvisited neighbours
#         unvstd_nghbrs = []
#         traversal_matrix = [(1,0),(-1,0),(0,1),(0,-1)]
#         for x_step, y_step in traversal_matrix:
#             nx, ny = x + x_step, y + y_step
#             if 0 <= nx < N and 0 <= ny < M:
#                 bit = 1 << (nx*M + ny)
#                 if not (mask & bit):
#                     unvstd_nghbrs.append((grid[nx][ny], nx, ny, bit))

#         # Explore in increasing-letter order
#         unvstd_nghbrs.sort()
#         for ch, nx, ny, bit in unvstd_nghbrs:
#             dfs(nx, ny, mask | bit, curr_string + ch)

#     # Kick off the search from (0,0)
#     dfs(0, 0, 1 << 0, grid[0][0])
#     return out_string

class SecretMessageFinder:
    def __init__(self, grid, N, M):
        self.grid = grid
        self.N = N
        self.M = M
        self.out_string = None

    def depthFirstSearch(self, i, j, mask, curr_string):
        # Base case (reached corner)
        if i == self.N - 1 and j == self.M - 1:
            if self.out_string is None or curr_string < self.out_string:
                self.out_string = curr_string
            return
        
        # Stop if prefix value is worse than out_sting
        if self.out_string is not None and curr_string > self.out_string[:len(curr_string)]:
            return

        unvstd_nghbrs = []
        traversal_matrix = [(1,0),(-1,0),
                            (0,1),(0,-1)]
        
        for move_i, move_j in traversal_matrix:
            next_i = i + move_i
            next_j = j + move_j

            if (0 <= next_i < self.N) and (0 <= next_j < self.M):
                bit_value = 1 << (next_i * self.M + next_j)
                if not (mask & bit_value):
                    unvstd_nghbrs.append((self.grid[next_i][next_j], next_i, next_j, bit_value))

        unvstd_nghbrs.sort()

        for next_char, next_i, next_j, bit_value in unvstd_nghbrs:
            self.depthFirstSearch(next_i, next_j, mask | bit_value, curr_string + next_char)

    def getSecretMessage(self):
        starting_mask = 1 << 0
        self.depthFirstSearch(0, 0, starting_mask, self.grid[0][0])
        return self.out_string
 

def main():

    N, M = inlt()
    inp_grid = [input().strip() for _ in range(N)]
    print(inp_grid)
    print(SecretMessageFinder(inp_grid, N, M).getSecretMessage())


if __name__ == '__main__':
    main()