import sys
from heapq import heappop, heappush
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

global MAX_LENGTH
MAX_LENGTH = 42195

def getMinCameras(n, cam_info):

    # Here, I am building intervals to check how much area each camera is covering
    # the start and end are capped at 0 and 42195(max length)
    intervals = []

    for x, k in cam_info:
        start = max(0, x - k)
        end = min(MAX_LENGTH, x + k)

        if start < end:
            intervals.append((start, end))

    intervals.sort(key=lambda r: r[0])
    print(intervals)

    int_len = len(intervals)
    selected_intervals = [False] * int_len

    max_heap = []
    min_heap = []

    idx, loc, final_cams = 0, 0, 0

    while loc < MAX_LENGTH:
        while idx < int_len  and intervals[idx][0] <= loc:
            start, end = intervals[idx]
            heappush(max_heap, (-end, idx)) # -ve is used to compensate for heappush only giving out min value in python. That's why I use abs operator later on
            idx += 1

        # print("Max Heap: ", max_heap)

        while min_heap and min_heap[0][0] <= loc:
            heappop(min_heap)

        # print("Min Heap: ",min_heap)

        depth = len(min_heap)
        while depth < 2:
            while max_heap:
                end, new_idx = heappop(max_heap)
                end = abs(end) # Converting back to positive
                if end <= loc or selected_intervals[new_idx]:
                    continue
                break
            else:
                return -1

            selected_intervals[new_idx] = True
            final_cams += 1
            heappush(min_heap, (end, new_idx))
            depth += 1

            # print("New Min Heap: ", min_heap)

        loc = min_heap[0][0]

    return final_cams


def main():

    n = inp()
    cam_info = []
    for _ in range(n):
        loc, rad = inlt()
        cam_info.append((loc, rad))

    # print(cam_info)

    print(getMinCameras(n, cam_info))


if __name__ == '__main__':
    main()