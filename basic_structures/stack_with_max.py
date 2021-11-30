
def execute(stack, max_stack, cmd):
    if cmd[0] == 'push':

        value = int(cmd[1])
        stack.append(value)

        if len(max_stack) == 0:
            max_stack.append(value)
        else:
            if max_stack[-1] < value:
                max_stack.append(value)
            else:
                max_stack.append(max_stack[-1])

    elif cmd[0] == 'pop':
        stack.pop()
        max_stack.pop()

    elif cmd[0] == 'max':
        print(max_stack[-1])


if __name__ == '__main__':

    n = int(input())
    stack = list()
    max_stack = list()
    for i in range(n):
        cmd = input().split()
        execute(stack, max_stack, cmd)