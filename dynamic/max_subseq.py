
def read_seq():
    n = int(input())
    seq = [int(x.strip()) for x in input().split()]
    assert n == len(seq)
    return seq


def get_size_of_max_subseq(seq):
    """ It finds the size of the max subseq, such that next element mod previous element = 0. """

    sizes = [1 for x in seq]
    for i in range(len(seq)):
        for j in range(0, i):
            if seq[i] % seq[j] == 0 and sizes[j]+1 > sizes[i]:
                sizes[i] += 1

    return max(sizes)


if __name__ == "__main__":

    seq = read_seq()
    print(get_size_of_max_subseq(seq))
