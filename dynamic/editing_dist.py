

def get_editing_distance(seq1, seq2):

    # initialise
    d = [[0 for x in range(len(seq2)+1)] for x in range(len(seq1)+1)]
    for i in range(len(seq1)+1):
        d[i][0] += i
    for j in range(len(seq2)+1):
        d[0][j] += j

    # fill in
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):

            diff = 0 if seq1[i-1] == seq2[j-1] else 1
            val = min(
                d[i-1][j]+1,
                d[i][j-1]+1,
                d[i-1][j-1]+diff
            )
            d[i][j] = val

    return d[-1][-1]


if __name__ == "__main__":

    seq1 = input().strip()
    seq2 = input().strip()
    print(get_editing_distance(seq1, seq2))