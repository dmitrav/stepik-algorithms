
def get_k_items(n):

    i = 1
    ans = []
    temp = n
    while True:
        if n - i < 0:
            if temp - sum(ans) > 0:
                ans.pop()
                ans.append(temp - sum(ans))
            return (i - 1, ans)
        n -= i
        ans.append(i)
        i += 1


if __name__ == "__main__":

    n = int(input())
    items = get_k_items(n)

    print(len(items))
    print(" ".join([str(x) for x in items]))
