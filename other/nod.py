
def gcd(a, b):

    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        a = a % b
    elif b >= a:
        b = b % a

    if a == 1 or b == 1:
        return 1
    else:
        return gcd(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()