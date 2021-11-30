

""" Disjoint sets """


def find(i, parents):
    while i != parents[i]:
        # parents[i] = find(parents[i], parents)  # supposedly, shortening paths
        i = parents[i]

    return i


def union(i, j, parents, ranks):
    i_id = find(i, parents)
    j_id = find(j, parents)
    if i_id == j_id:
        return

    if ranks[i_id] > ranks[j_id]:  # joining by ranks
        parents[j_id] = i_id
    else:
        parents[i_id] = j_id
        if ranks[i_id] == ranks[j_id]:
            ranks[j_id] += 1


if __name__ == '__main__':

    n, e, d = [int(x) for x in input().split()]

    parents = [x for x in range(n)]
    ranks = [0] * n

    correct = True

    for _ in range(e):
        x_i, x_j = [int(x) - 1 for x in input().split()]
        union(x_i, x_j, parents, ranks)

    for _ in range(d):
        x_i, x_j = [int(x) - 1 for x in input().split()]
        par_i = find(x_i, parents)
        par_j = find(x_j, parents)
        if par_j == par_i:
            correct = False
            break

    print(int(correct))