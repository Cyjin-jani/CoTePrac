class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def changePostfix(S):
    answer = ''
    opStack = ArrayStack()
    for c in S:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        elif c not in prec:
            answer += c
        else:
            if opStack.isEmpty():
                opStack.push(c)
            else:
                while prec[c] <= prec[opStack.peek()]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
                opStack.push(c)

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


changePostfix("A+B*C")
