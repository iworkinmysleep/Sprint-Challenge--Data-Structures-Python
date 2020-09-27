class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    
class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return

        prev = None
        current_node = self.head

        # loop until the head reaches None
        while current_node is not None:
            # handle the next node added
            node = current_node.get_next()
            # change the next node to be the previous node 
            current_node.set_next(prev)
            # change the previous node to be the current node
            prev = current_node
            # change the current node to be the next node added 
            current_node = node
        # change the previous node to be the head, this makes the head None
        self.head = prev
        
            
