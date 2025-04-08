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


def DFS(tree, removed_bool,visited, node):
    visited[node] = True
    size = 1 
    for neighbor in tree[node]:
        if not removed_bool[neighbor] and not visited[neighbor]:
            size += DFS(tree, removed_bool, visited, neighbor)
    return size

def getMaxComponents(n, parents, removed_nodes):
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        parent = parents[i - 1]  
        tree[parent].append(i)
        tree[i].append(parent) 
    
    removed_bool = [False] * n
    for node in removed_nodes:
        removed_bool[node] = True
    
    visited = [False] * n
    max_component_size = 0
    
    for i in range(n):
        if not removed_bool[i] and not visited[i]:
            component_size = DFS(tree,removed_bool, visited, i)
            max_component_size = max(max_component_size, component_size)
    
    return max_component_size


if __name__ == '__main__':

    n, m = inlt()

    parents = []
    for i in range(n - 1):
        parents.append(inp())

    traitors = []
    for i in range(m):
        traitors.append(inp())

    print(getMaxComponents(n, parents, traitors))