class HashTable():
    def __init__(self, size):
        self.data = [None] * size
        self.flag = [None] * size
        self.cnt = 0

    def insert(self, s):
        ind = hash_func(s)
        ind = re