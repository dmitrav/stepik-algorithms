

def fib_n_mod_m():

    n, m = map(int, input().split())

    if n <= 2:
        return 1

    else:

        mods = [0, 1]
        for i in range(2, m*m+1):  # not until n, because i don't remember why
            mods.append((mods[i-1] % m + mods[i-2] % m) % m)
            if mods[i] == 1 and mods[i-1] == 0:
                # pisano period
                break
        mods = mods[:-2]

        print(mods)
        print(n)
        print(n % len(mods))

        return mods[n % len(mods)]


if __name__ == '__main__':

    print(fib_n_mod_m())