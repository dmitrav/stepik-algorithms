
def read_points():
    n = int(input())
    segments = []
    for i in range(n):
        segment = [int(x) for x in input().split()]
        segments.append(tuple(segment))

    return segments


def insertion_sort(segments):
    # sort by right end
    for j in range(1, len(segments)):
        key = segments[j]
        i = j - 1
        while i >= 0 and segments[i][1] > key[1]:
            segments[i + 1] = segments[i]
            i = i - 1
        segments[i + 1] = key
    return segments


def assign_points(sorted_segments):

    # now the algorithm itself
    points = [sorted_segments[0][1]]
    i = 1
    while i < len(sorted_segments):
        if sorted_segments[i][0] <= points[-1] <= sorted_segments[i][1]:
            pass
        else:
            points.append(sorted_segments[i][1])
        i += 1

    return points


if __name__ == '__main__':

    segments = read_points()
    sorted_segments = insertion_sort(segments)
    points = assign_points(sorted_segments)

    print(len(points))
    print(" ".join([str(x) for x in points]))