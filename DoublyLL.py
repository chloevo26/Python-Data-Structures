class DoublylinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = DoublylinkedListNode(1)
b = DoublylinkedListNode(2)
c = DoublylinkedListNode(3)

a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b