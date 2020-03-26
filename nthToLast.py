class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head
    for i in range(n-1):
        # if right_pointer == None
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')
        right_pointer = right_pointer.nextnode

    while(right_pointer.nextnode):
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    return left_pointer
