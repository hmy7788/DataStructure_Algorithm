# append, insert, pop, remove, find 구현
class Array:
    def __init__(self, capacity):
        self.capacity = capacity    # array의 크기
        self.size = 0   # 데이터의 개수
        self.array = [None] * capacity  # 리스트로 구현

    def _resize(self):  # append, insert시 capacity 크기 증가 메소드
        self.capacity *= 2  # capacity 2배로 증가
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def append(self, value):
        if(self.size == self.capacity): # 사이즈와 용량 체크
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, i, value):
        if(i < 0 or i > self.size): # 인덱스 체크
            return False
        if(self.size == self.capacity):
            self._resize()
        for j in range(self.size, i-1, -1): # 뒤 -> 앞 덮어쓰기
            self.array[j] = self.array[j-1]
        self.array[i] = value
        self.size += 1
        
    def pop(self, i=None):
        if(self.size == 0):
            return False
        if(i < 0 or i > self.size): # 인덱스 체크
            return False
        if(i == None):  # i의 default값 조정
            i = self.size-1
        rv = self.array[i]
        for j in range(i, self.size-1): # 앞 -> 뒤 덮어쓰기
            self.array[j] = self.array[j+1]
        self.array[self.size-1] = None  # 맨 끝값 None 해주기 
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
        if(self.size == 0):
            return 'Empty Array'
        return ' '.join(str(self.array[i]) for i in range(self.size))