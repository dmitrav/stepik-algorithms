import sys

sys.setrecursionlimit(20000)


def get_h(vertex, parents, heights):
    min_h = 1
    if parents[vertex] == -1:
        return min_h
    else:
        if heights[vertex] > 0:
            return heights[vertex]
        else:
            return min_h + get_h(parents[vertex], parents, heights)


def get_tree_height(size, parents):
    heights = [0 for x in range(size)]
    for i in range(size):
        h = get_h(i, parents, heights)
        heights[i] = h

    return max(heights)


if __name__ == '__main__':

    size = int(input())
    parents = [x for x in map(int, input().split())]

    print(get_tree_height(size, parents))