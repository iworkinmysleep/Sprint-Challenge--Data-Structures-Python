class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.items = []
                    

    def append(self, item):
        # if array is full, manipulate the index of the item before appending
        if len(self.items) == self.capacity:
            self.items[self.index] = item
            self.index = (self.index + 1) % self.capacity
        else:
            self.items.append(item)


    def get(self):
        return self.items