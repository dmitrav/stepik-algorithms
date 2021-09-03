
import math, heapq

if __name__ == "__main__":

    n = 100000

    d = {
        'n/log5n': lambda x: x / math.log(x, 5),
        '2^n': lambda x: 2 ** x,
        'log2n!': lambda x: math.log2(math.factorial(x)),
        'log3n': lambda x: math.log(x, 3),
        'log2log2n': lambda x: math.log2(math.log2(x)),
        '7^log2n': lambda x: 7 ** (math.log2(x)),
        '4^n': lambda x: 4 ** x,
        '3^log2n': lambda x: 3 ** (math.log2(x)),
        'n!': lambda x: math.factorial(x),
        'sqrt(n)': lambda x: math.sqrt(x),
        'log2n^(log2n)': lambda x: math.log2(x ** (math.log2(x))),
        'sqrt(log4n)': lambda x: math.sqrt(math.log(x, 4)),
        'n^(log2n)': lambda x: x ** (math.log2(x)),
        '2^3n': lambda x: 2 ** (3 * x),
        'n^sqrt(n)': lambda x: x ** (math.sqrt(x)),
        '(log2n)^2': lambda x: math.log2(x) ** 2,
        'n^2': lambda x: x * x
    }

    h = []
    for f in d:
        h.append((d[f](n), f))

    # build a heap to sort
    heapq.heapify(h)

    while len(h) > 0:
        # print the sorted order
        print(heapq.heappop(h)[1])



