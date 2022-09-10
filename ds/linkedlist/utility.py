from linkedlist import create

class Utility:
    def insert_at_front(self, data, head):
        '''
        -Insert and data at the begining of the linked list
        '''
        node = create.Node(data, head)
        head = node

    def append_at_end(self, data, head):
        '''
        -Insert and data at the end of the linked list
        '''
        if head is None:
            head = create.Node(data, None)
            return
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = create.Node(data, None)

    def print_linked_list(self, head):
        '''
        -Print the linked list
        -Return: string
        '''
        if head is None:
            print("linked list is empty")
            return
        cur = head
        strin = ""
        while cur:
            strin += str(cur.data) + '--'
            cur = cur.next
        return lis

    def complete_reverse(self, head):
        '''
        -Revese the linked list comletely
        -Return: head node
        '''
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev