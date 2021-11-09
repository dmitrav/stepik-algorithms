

if __name__ == '__main__':

    n = int(input())

    steps = [0] + [10**5 for x in range(n-1)]
    prevs = [0 for x in range(n)]

    for i in range(1,n+1):
        for k in (i+1, i*2, i*3):

            if k < 1+n and steps[i-1] + 1 < steps[k-1]:
                steps[k-1] = steps[i-1] + 1
                prevs[k-1] = i

    ans = [n]
    while n > 1:
        ans.append(prevs[n-1])
        n = prevs[n-1]

    print(len(ans)-1)
    print(*list(reversed(ans)))