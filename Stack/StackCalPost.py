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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for c in tokenList:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif c not in prec:
            postfixList.append(c)
        else:
            if opStack.isEmpty():
                opStack.push(c)
            else:
                while prec[c] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(c)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    calStack = ArrayStack()
    result = 0

    for item in tokenList:

        if item == '+':
            num1 = calStack.pop()
            num2 = calStack.pop()
            val = num1 + num2
            calStack.push(val)

        elif item == '-':
            num1 = calStack.pop()
            num2 = calStack.pop()
            val = num2 - num1
            calStack.push(val)

        elif item == '*':
            num1 = calStack.pop()
            num2 = calStack.pop()
            val = num1 * num2
            calStack.push(val)

        elif item == '/':
            num1 = calStack.pop()
            num2 = calStack.pop()
            val = num2 / num1
            calStack.push(val)

        else:
            calStack.push(item)

    result = calStack.pop()

    return result


def calculatePost(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return print("계산결과", val)


calculatePost("4*(3+5)")
