class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def linked_list(lis):
        node = Node(lis[0])
        head = node
        for i in range(1, len(lis)):
            node.next = Node(lis[i])
            node = node.next
        return head

    
    