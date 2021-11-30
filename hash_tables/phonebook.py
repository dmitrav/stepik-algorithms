
""" Direct addressing. """


def execute(cmd, book):

    if cmd.split()[0] == 'add':
        key = int(cmd.split()[1]) - 1
        book[key] = cmd.split()[2]
    elif cmd.split()[0] == 'find':
        key = int(cmd.split()[1]) - 1
        name = book[key]
        if name is None:
            print('not found')
        else:
            print(name)
    elif cmd.split()[0] == 'del':
        key = int(cmd.split()[1]) - 1
        book[key] = None


if __name__ == "__main__":
    n = int(input())
    book = [None] * (10 ** 7)
    for i in range(n):
        cmd = input()
        execute(cmd, book)