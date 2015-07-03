def calc(eq):
    stack = []
    for i in range(len(eq)):
        if eq[i].isdigit():
            stack.append(int(eq[i]))
        elif eq[i] == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif eq[i] == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif eq[i] == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        elif eq[i] == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
    return stack.pop()


def main():
    eq = raw_input().split()
    print calc(eq)

if __name__ == '__main__':
    main()
