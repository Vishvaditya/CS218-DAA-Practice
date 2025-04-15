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



def getMaxCandleNumber(budget, price):
    min_price = min(price)

    max_digits = budget//min_price

    out_number = ""

    price_dict = {}

    for i in range(1, len(price)+1):
        price_dict[i] = price[i-1]

    remaining_digits = max_digits
    for digits in range(1, max_digits+1):
        remaining_digits -= 1
        for j in range(9, 0, -1):
            if (budget-price_dict[j])//min_price>= remaining_digits:
                out_number += str(j)
                budget -= price_dict[j]
                

    return out_number


def main():

    budget = inp()
    price = inlt()
    print(getMaxCandleNumber(budget, price))


if __name__ == '__main__':
    main()