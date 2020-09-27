class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = -1
        self.items = []
                    

    def append(self, item):
        if len(self.items) == self.capacity:
            self.current = (self.current + 1) % self.capacity
            self.items[self.current] = item
        else:
            self.items.append(item)


    def get(self):
        return self.items