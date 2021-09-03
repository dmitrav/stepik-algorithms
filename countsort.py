

def read_numbers():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    assert n == len(numbers)
    return numbers


def countsort(numbers):
    """ This is just counting and imputing. """

    counts = [0 for x in range(10)]  # all numbers are from [1, 10]
    for n in numbers:
        counts[n-1] += 1

    numbers = []
    for i in range(len(counts)):
        numbers.extend([i+1 for x in range(counts[i])])

    return numbers


def stable_countsort(numbers):

    counts = [0] * 10

    for j in range(len(numbers)):
        counts[numbers[j]-1] += 1

    # build cumulative counts
    for i in range(1, 10):
        counts[i] = counts[i-1] + counts[i]

    sorted_numbers = [0] * len(numbers)
    for i in reversed(range(len(numbers))):
        sorted_numbers[counts[numbers[i]-1]-1] = numbers[i]
        counts[numbers[i]-1] -= 1

    return sorted_numbers


if __name__ == "__main__":
    numbers = read_numbers()
    sorted_numbers = stable_countsort(numbers)
    print(" ".join([str(x) for x in sorted_numbers]))