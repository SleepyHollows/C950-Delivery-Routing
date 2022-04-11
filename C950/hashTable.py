class HashMap:
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

    # O(1) Complexity 
    # Making hash keys
    def createHashKey(self, key):
        return int(key) % len(self.map)

    # O(n) Complexity
    # Appending packages into hash table
    def insert(self, key, value):
        keyHash = self.createHashKey(key)
        keyValue = [key, value]

        if self.map[keyHash] == None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = keyValue
                    return True
            self.map[keyHash].append(keyValue)
            return True

    # O(n) Complexity
    # Updating packages in hash table
    def update(self, key, value):
        keyValue = self.createHashKey(key)
        if self.map[keyValue] is not None:
            for pair in self.map[keyValue]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print("Error, didn't update on key: " + key)

    # O(n) Complexity
    # Get the values from hash table using linked keys
    def getValue(self, key):
        keyHash = self.createHashKey(key)
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # O(n) Complexity
    # Poping a value from the hash table
    def delete(self, key):
        keyHash = self.createHashKey(key)

        if self.map[keyHash] is None:
            return False
        for i in range(0, len(self.map[keyHash])):
            if self.map[keyHash][i][0] == key:
                self.map[keyHash].pop(i)
                return True
        return False

class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
