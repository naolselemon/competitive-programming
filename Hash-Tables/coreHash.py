class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for ch in key:
            hash  = (hash + ord(ch) *  31) % len(self.data) # Using a prime number 31 for better distribution and modulo to fit in array size
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        if(self.data[address] is None):
            self.data[address] = []
        self.data[address].append([key, value])
        # print(f"Key {key} has been added at address {address}")
        # print(self.data)
        return self.data
    
    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket is None:
            return None
        for k, v in currentBucket:
            if k == key:
                return v
        return None


newHashTable = HashTable(50)
newHashTable.set("grapes", 10000)
newHashTable.set("apples", 54)
print(newHashTable.get("grapes"))  # Output: 10000


