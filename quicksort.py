import random


def partition3(A, l, r):

    lt = l
    i = l
    gt = r
    support = A[l]
    while i <= gt:
        if A[i] < support:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > support:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def quicksort(A, l, r):

    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]

    lt, gt = partition3(A, l, r)
    quicksort(A, l, lt - 1)
    quicksort(A, gt + 1, r)


if __name__ == "__main__":

    a = [3, 2, 0, 4, 2, 8, 8, 8, 24, 23, 29]
    quicksort(a, 0, len(a) - 1)
    print(a)
