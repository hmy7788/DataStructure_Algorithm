# append, insert, remove, pop, find 구현
class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def append(self, value):
        if(self.size == self.capacity):
            self._resize()
        self.array[self.size] = value
        self.size += 1
    
    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def remove(self, value):
        pass