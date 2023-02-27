class HashMap():
    def __init__(self, size, ) -> None:
        self.size = size
        self.internalArray = [[] for _ in range(self.size)]
    
    def setValue(self, key, value) -> None:
        hashKey = hash(key) % self.size
        hashBucket = self.internalArray[hashKey]
        foundKey = False
        for index, item in enumerate(hashBucket):
            itemKey, itemVal = item
            if itemKey == key:
                foundKey == True
                break
        if foundKey:
            hashBucket[index] = (key, value)
        else:
            hashBucket.append((key, value))
    
    def incrementValue(self, key) -> None:
        # Key MUST be short, int, long, etc.
        hashKey = hash(key) % self.size
        hashBucket = self.internalArray[hashKey]
        foundKey = False
        for index, item in enumerate(hashBucket):
            itemKey, itemVal = item
            if itemKey == key:
                hashBucket[index][1] += 1
                return
        print("No value found")

    def get_val(self, key) -> int:
        hashKey = hash(key) % self.size
        for index, item in enumerate(self.internalArray[hashKey]):
            itemKey, itemVal = item
            if itemKey == key:
                return itemVal
        print("No value found")
    
    def deleteValue(self, key) -> None:
        hashKey = hash(key) % self.size
        hashBucket = self.internalArray[hashKey]
        for index, item in enumerate(hashBucket):
            itemKey, itemVal = item
            if itemKey == key:
                hashBucket.pop(index)
                return
        print("Value not found")

    def __str__(self) -> str:
        return "".join(str(item) for item in self.internalArray)