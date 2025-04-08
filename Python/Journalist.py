import sys
import heapq
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


def getShortestPath(roads, start):
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_dist > distances[curr_node]:
            continue
        
        for neighbor, dist in roads[curr_node]:
            distance = curr_dist + dist
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def getMaxDist(n, edges, venues):

    roads = [[] for _ in range(n)]
    for u, v, l in edges:
        roads[u].append((v, l))
        roads[v].append((u, l))  
        
    max_dist = 0
    for i in range(len(venues)):
        distances = getShortestPath(roads, venues[i])
        for j in range(len(venues)):
            if i != j:
                max_dist = max(max_dist, distances[venues[j]])

    return max_dist


if __name__ == '__main__':
    n, m = inlt()
    num_venues = inp()
    venues = inlt()
    t = inp()

    edges = []
    for _ in range(m):
        u, v, l = inlt()
        edges.append((u,v,l))

    max_dist = getMaxDist(n, edges, venues)
    speed = round(max_dist/(t*60), 3)
    print("{:.3f}\n".format(speed))


