class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def reverse(head):
    current = head
    previous = None
    nextNode = None

    while(current):
        nextNode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextNode
    return previous

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)







