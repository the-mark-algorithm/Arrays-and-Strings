# Implement an algorithm to determine if a string has all unique characters.
# What if you can't use additional data structures?
import sys
from collections import defaultdict

class HashTable:
    keys = list()
    vals = list()

    def __init__(self, size) -> None:
        for i in range(size):
            self.vals.append(None)

        self.size = size

    def add(self, key, val):
        if key not in self.keys: # Should we care about duplicate keys?
            self.keys.append(key)
        
        
def isUnique(useDataStructures: bool, string: str):
    if useDataStructures:
        alphabet = defaultdict(int)
        for s in string:
            if alphabet[s] > 0: # already found an instance, not unique
                return False
            alphabet[s] += 1
        return True
    else: #todo make own hash table

        pass

def main():
    # argv = [ isUnique.py, useDataStrucutures (T/F), Word (String) ]

    pass

if __name__ == "__main__":
    main()