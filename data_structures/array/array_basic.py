# append, insert, pop, remove, find 구현
class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def append(self, value):
        if(self.size == self.capacity):
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, i, value):
        if(i < 0 or i > self.size):
            return False
        if(self.size == self.capacity):
            self._resize()
        for j in range(self.size, i-1, -1):
            self.array[j] = self.array[j-1]
        self.array[i] = value
        self.size += 1
        
    def pop(self, i=None):
        if(self.size == 0):
            return False
        if(i < 0 or i > self.size):
            return False
        if(i == None):
            i = self.size-1
        rv = self.array[i]
        for j in range(i, self.size-1):
            self.array[j] = self.array[j+1]
        self.array[self.size-1] = None
        self.size -= 1
        return rv

    def remove(self, value):
        if(self.size == 0):
            return False
        for i in range(self.size):
            if(self.array[i] == value):
                for j in range(i, self.size-1):
                    self.array[j] = self.array[j+1]
                self.array[self.size-1] = None
                self.size -= 1
                return i
            
    def find(self, value):
        for i in range(self.size):
            if(self.array[i] == value):
                return i
        return False

    def __str__(self):
        string = ''
        if(self.size == 0):
            return 'Empty Array'
        for i in self.array:
            if(i != None):
                string += str(i) + ' '
        return string