import re

expr = '6 + 15 - 4 + 17'

s = list(expr)
tokens = [x.strip() for x in re.split('(\d+)', expr) if x.strip() != '']

opStack = []
valStack = []

for t in tokens:
        if t.isdigit():
                valStack.append(int(t))
        else:
                opStack.append(t)

while len(opStack) != 0:
        op = opStack.pop(0)
        v1 = valStack.pop(0)
        v2 = valStack.pop(0)

        if op == '+':
                valStack.insert(0, v1 + v2)
        if op == '-':
                valStack.insert(0, v1 - v2)

print(valStack[0])
