import sys
import bisect
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

INF = 10**16

class SegTree:
    """A segment tree for (min_defense, index) on a fixed array."""
    def __init__(self, data):
        self.n = len(data)
        self.size = 1

        while self.size < self.n:
            self.size <<= 1

        self.tree = [(INF, -1)] * (2 * self.size)

        for i, val in enumerate(data):
            self.tree[self.size + i] = (val, i)

        for p in range(self.size - 1, 0, -1):
            self.tree[p] = min(self.tree[2*p], self.tree[2*p + 1])

    def query(self, l, r):

        if l > r:
            return (INF, -1)
        
        res = (INF, -1)
        l += self.size
        r += self.size

        while l <= r:
            if (l & 1):
                res = min(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = min(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1

        return res

    def remove(self, idx):
        p = self.size + idx
        self.tree[p] = (INF, idx)
        p >>= 1
        while p:
            self.tree[p] = min(self.tree[2*p], self.tree[2*p + 1])
            p >>= 1


def main():
    n = inp()
    cars = []
    for _ in range(n):
        x, d = map(int, input().split())  
        cars.append((x, d))

    # Read attacks
    m = int(input())
    attacks = []
    for _ in range(m):
        a, b, y = map(int, input().split())  
        attacks.append((a, b, y))


    cars.sort(key=lambda t: t[0])
    positions = [c[0] for c in cars]   # xi in sorted order
    defenses = [c[1] for c in cars]    # Di in the same order

    seg = SegTree(defenses)


    out = []
    for Aj, bj, yj in attacks:

        L = yj - bj
        R = yj + bj

        l = bisect.bisect_left(positions, L)
        r = bisect.bisect_right(positions, R) - 1

        destroyed = 0
        while True:
            d_min, idx = seg.query(l, r)
            if d_min <= Aj:
                destroyed += 1
                seg.remove(idx)
            else:
                break

        out.append(str(destroyed))

    print("\n".join(out))


if __name__ == "__main__":
    main()
