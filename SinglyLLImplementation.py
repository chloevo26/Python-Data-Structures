class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):       # add node at the front
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insertAfter(self, prev_node, new_data):
        # check if the given node exist
        if prev_node is None:
            print('The previous node must in Linked List')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        current =  self.head
        while(current.next):
            current = current.next

        current.next = new_node

    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def reverse(self):
        curr = self.head
        next = self.head.next
        next2node = self.head.next.next

        while (next2node.next):
            next.next = curr
            curr = next
            next = next2node
            next2node = next2node.next
        next.next = curr
        next2node.next = next
        self.head.next = None
        self.head = next2node




if __name__ == '__main__':
    llist = LinkList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    print('Created linked list is: ')
    llist.printList()
    print('------------------')
    llist.reverse()
    llist.printList()

