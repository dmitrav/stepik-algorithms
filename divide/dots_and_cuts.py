
from sort.quicksort import quicksort
from bisect import bisect_left


def read_input():
    n_cuts, n_dots = [int(x) for x in input().split()]

    first_ps = []
    last_ps = []
    for i in range(n_cuts):
        first, last = [int(x) for x in input().split()]
        first_ps.append(first)
        last_ps.append(last)

    dots = [int(x) for x in input().split()]
    assert n_dots == len(dots)

    return first_ps, last_ps, dots


def quick_partition(arr, left=True):
    """ Make a partition as in 2-way quicksort to find elements smaller than the first one in arr.
        Still SLOW. """

    i, li = 1, 0
    dot = arr[li]
    while i <= len(arr)-1:
        if left:
            if arr[i] <= dot:
                arr[i], arr[li] = arr[li], arr[i]
                i += 1
                li += 1
            else:
                break
        else:
            if arr[i] < dot:
                arr[i], arr[li] = arr[li], arr[i]
                i += 1
                li += 1
            else:
                break
    return li


def count_bounds_left_slow(dot, left_bounds):
    """ This method is SLOW. It results in time limit exceeded. """
    count = 0
    for bound in left_bounds:
        if bound <= dot:
            # left bound is actually on the left
            count += 1
        else:
            break
    return count


def count_bounds_right_slow(dot, right_bounds):
    """ This method is SLOW. It results in time limit exceeded. """
    count = 0
    for bound in right_bounds:
        if bound < dot:
            # left bound is actually on the left
            count += 1
        else:
            break
    return count


def count_bounds_left(dot, left_bounds):

    arr = [dot, *left_bounds]
    return quick_partition(arr, left=True)


def count_bounds_right(dot, right_bounds):

    arr = [dot, *right_bounds]
    return quick_partition(arr, left=False)


def first_approach():
    """ Too slow... time limit exceeded. """

    left_bounds, right_bounds, dots = read_input()

    quicksort(left_bounds, 0, len(left_bounds) - 1)
    quicksort(right_bounds, 0, len(right_bounds) - 1)

    intersections = []
    for dot in dots:
        lc = count_bounds_left(dot, left_bounds)
        rc = count_bounds_right(dot, right_bounds)
        print('lc={}, rc={}'.format(lc, rc))
        intersections.append(lc - rc)

    print(" ".join([str(x) for x in intersections]))


if __name__ == "__main__":

    left_bounds, right_bounds, dots = read_input()

    quicksort(left_bounds, 0, len(left_bounds)-1)
    quicksort(right_bounds, 0, len(right_bounds)-1)

    intersections = []
    for dot in dots:
        # apply binary search to find how many element are smaller than the dot
        lc = bisect_left(left_bounds, dot+1)
        rc = bisect_left(right_bounds, dot)
        intersections.append(lc-rc)

    print(" ".join([str(x) for x in intersections]))