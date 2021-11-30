x = 263
p = 1000000007


def get_hash(string, m, degrees):
    # polynomial hashing
    h = 0
    for i in range(len(string)):
        h += ord(string[i]) * (degrees[i] % p)

    h = h % p
    return h % m


def execute(cmd, hash_table, m, degrees):
    cmd = cmd.split()

    if cmd[0] == 'add':
        h = get_hash(cmd[1], m, degrees)
        if cmd[1] in hash_table[h]:
            return
        else:
            # chaining to resolve collisions
            hash_table[h].append(cmd[1])

    elif cmd[0] == 'del':
        h = get_hash(cmd[1], m, degrees)
        if cmd[1] in hash_table[h]:
            hash_table[h].remove(cmd[1])
        else:
            return

    elif cmd[0] == 'find':
        h = get_hash(cmd[1], m, degrees)
        if cmd[1] in hash_table[h]:
            print('yes')
        else:
            print('no')

    elif cmd[0] == 'check':
        print(*reversed(hash_table[int(cmd[1])]))


if __name__ == "__main__":

    m = int(input())
    n = int(input())

    degrees = [x ** d for d in range(15)]
    hash_table = [[] for x in range(m)]

    for i in range(n):
        cmd = input()
        execute(cmd, hash_table, m, degrees)