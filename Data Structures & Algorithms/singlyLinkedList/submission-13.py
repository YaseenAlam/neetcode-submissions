class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, index: int) -> bool:
        current = self.head
        count = 0

        if current is None:
            return False
        

        if index == 0:
            self.head = self.head.next
            return True

        while current and count < index - 1:
            current = current.next
            count += 1
        
        if current is None or current.next is None:
            return False
        
        target = current.next
        current.next = target.next
        target = None
        return True

    def getValues(self) -> List[int]:
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next
        return nodes