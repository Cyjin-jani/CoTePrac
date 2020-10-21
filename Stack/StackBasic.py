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

# 연결리스트를 이용한 스택의 구현
# class LinkedListStack:

#     def __init__(self):
#         self.data = DoublyLinkedList()

#     def size(self):
#         return self.data.getLength()

#     def isEmpty(self):
#         return self.size() == 0

#     def push(self, item):
#         node = Node(item)
#         self.data.insertAt(self.size() + 1, node)

#     def pop(self):
#         return self.data.popAt(self.size())

#     def peek(self):
#         return self.data.getAt(self.size()).data


# 수식 올바른지 판단하는 함수.
def checkFormulaRight(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = match[c]
                if t != S.pop():
                    return False

    return S.isEmpty()
