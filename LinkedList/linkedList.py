# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # 리스트 원소 찾기
    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # 리스트 순회
    def traverse(self):
        array = []
        curr = self.head
        while curr:
            array.append(curr.data)
            curr = curr.next
        return array

    # 리스트 길이
    def getLength(self):
        return self.nodeCount

    # 리스트에 원소 추가
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # 리스트 원소 삭제
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = self.getAt(pos)

        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        elif pos == 1:
            self.head = curr.next
        else:
            prev = self.getAt(pos-1)
            if pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    # 두 리스트 합치기
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
