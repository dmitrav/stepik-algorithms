
def read_array():
    s = input().split()
    n = int(s[0])
    arr = [int(x) for x in s[1:]]
    assert len(arr) == n
    return arr


def binary_search(arr, el):

    l = 0
    r = len(arr)-1

    while l <= r:
        m = int(l + (r - l) / 2)
        if arr[m] == el:
            return m+1
        elif arr[m] < el:
            l = m+1
        else:
            r = m-1
    return -1


if __name__ == "__main__":

    A = read_array()
    B = read_array()

    for el in B:
        print(binary_search(A, el), end=" ")
