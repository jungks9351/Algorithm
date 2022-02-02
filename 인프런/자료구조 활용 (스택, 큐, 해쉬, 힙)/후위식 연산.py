import sys

sys.stdin = open('input.text')

postfix = input()

res = 0
stack = []

for x in postfix:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x =='/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)

print(stack[0])
