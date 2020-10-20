class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    # 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    # 역순회
    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    # 특정 원소 찾기
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    # 리스트 원소 삽입 (특정 원소 뒤)
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    # 리스트 원소 삽입 (특정 순서에)
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # 리스트 원소 삽입 (특정 원소 앞에)
    def insertBefore(self, next, newNode):
        prev = next.prev
        prev.next = newNode
        next.prev = newNode
        newNode.prev = prev
        newNode.next = next
        self.nodeCount += 1
        return True

    # 리스트 원소 삭제(특정 원소 뒤)
    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    # 리스트 원소 삭제(특정 원소 앞)
    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        next = next
        next.prev = prev
        prev.next = next
        self.nodeCount -= 1
        return curr.data

    # 리스트 원소 삭제 (특정 순서)

    def popAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        curr = prev.next
        next = curr.next
        if pos > self.nodeCount // 2:
            return self.popAfter(prev)
        else:
            return self.popBefore(next)

    # 리스트 연결
    def concat(self, L):
        prev = self.tail.prev
        next = L.head.next
        prev.next = L.head.next
        next.prev = prev
        self.tail = L.tail
        L.head = self.head
        self.nodeCount += L.nodeCount
