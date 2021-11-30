

def heapify(arr, n, i, pairs):
    # essentially, this is sift down

    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        pairs.append((i, smallest))

        heapify(arr, n, smallest, pairs)


def build_heap(arr, n):
    # index of last non-leaf node
    start_index = n // 2 - 1

    pairs = []
    for i in range(start_index, -1, -1):
        heapify(arr, n, i, pairs)

    return pairs


if __name__ == '__main__':

    n = int(input())
    arr = [x for x in map(int, input().split())]

    pairs = build_heap(arr, n)

    print(len(pairs))
    if len(pairs) > 0:
        for pair in pairs:
            print(*pair)