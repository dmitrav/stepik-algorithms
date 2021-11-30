from collections import deque


def get_moving_max_2(array, size, wsize):
    d = deque()

    for i in range(wsize):

        # keep the decreasing order in d
        while len(d) > 0 and array[i] >= array[d[-1]]:
            d.pop()
        d.append(i)

    moving_max = list()

    for i in range(wsize, size):

        # largest is on the left
        moving_max.append(array[d[0]])

        # drop elements that are outside the window
        while len(d) > 0 and d[0] <= i - wsize:
            d.popleft()

        # keep the decreasing order in d
        while len(d) > 0 and array[i] >= array[d[-1]]:
            d.pop()
        d.append(i)

    moving_max.append(array[d[0]])

    return moving_max


if __name__ == '__main__':

    size = int(input())
    array = [x for x in map(int, input().split())]
    wsize = int(input())

    print(*get_moving_max_2(array, size, wsize))