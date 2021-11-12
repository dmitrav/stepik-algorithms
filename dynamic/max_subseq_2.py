
def read_seq():
    n = int(input())
    seq = [int(x.strip()) for x in input().split()]
    assert n == len(seq)
    return seq


def get_max_subseq(seq):
    """ It finds the max subseq, such that next element <= previous element.
        Here O(n^2) is SLOw, time limit exceeded. """

    sizes = [1 for x in seq]
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[i] <= seq[j] and sizes[j]+1 > sizes[i]:
                sizes[i] += 1

    k = sizes.index(max(sizes))
    indices = [k]
    # k is gonna be the current max
    j = k-1
    while j >= 0:
        if sizes[j]+1 == sizes[k]:
            indices.append(j)
            k = j
        j -= 1

    return len(indices), indices


def get_max_subseq_2(seq):
    """ With binary search. """

    n = len(seq)
    L = [1000] + [-1000] * (n+1)
    prev = []
    for i in range(n):

        left = 0
        right = n+1
        # binary search
        while left+1 < right:
            middle = (left + right) // 2
            if L[middle] >= seq[i]:
                left = middle
            else:
                right = middle
        L[right] = seq[i]
        prev.append((right, i, seq[i]))

    # print(L)
    # print(prev)

    i = n + 1
    # find the max length
    while L[i] == -1000:
        i -= 1

    ans = []
    j = len(prev)-1
    # starting from previously found i
    while j >= 0:
        if prev[j][0] == i:
            ans.append(prev[j][1]+1)
            i -= 1
        j -= 1

    return ans


def print_(size, indices):
    """ Print the size and the indices in the ascending order (as they are found in the descending order). """

    print(size)
    i = size - 1
    while i >= 0:
        print(indices[i] + 1, end=" ")
        i -= 1


if __name__ == "__main__":

    seq = read_seq()
    subseq = get_max_subseq_2(seq)

    print(len(subseq))
    for i in reversed(range(len(subseq))):
        print(subseq[i], end=' ')

