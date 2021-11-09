

if __name__ == '__main__':

    n = int(input())
    stairs = [int(x) for x in input().split()]

    if len(stairs) > 1:
        s = [stairs[0], max(stairs[1], stairs[0] + stairs[1])]
        if len(stairs) > 2:
            i = 2
            while i < len(stairs):
                s.append(max(stairs[i] + s[i-1], stairs[i] + s[i-2]))
                i += 1
    else:
        s = stairs

    print(s[-1])
