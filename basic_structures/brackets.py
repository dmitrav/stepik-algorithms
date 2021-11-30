
def check_brackets(s):
    stack = list()

    i = 0
    unmatched = list()
    while i < len(s):

        if s[i] in ['(', '{', '[']:
            stack.append(s[i])
            unmatched.append(i + 1)
        elif s[i] in [')', '}', ']']:
            if len(stack) == 0:
                return i + 1
            else:
                last = stack.pop()
                if s[i] == ')' and last == '(':
                    unmatched.pop()
                elif s[i] == '}' and last == '{':
                    unmatched.pop()
                elif s[i] == ']' and last == '[':
                    unmatched.pop()
                else:
                    return i + 1
        else:
            pass
        i += 1

    return 'Success' if len(stack) == 0 else unmatched.pop()


if __name__ == '__main__':

    s = input()
    print(check_brackets(s))