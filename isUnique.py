# Implement an algorithm to determine if a string has all unique characters.
# What if you can't use additional data structures?
import sys

class HashTable:
    keys = list()
    vals = list()

    # for alphabet hash function is just its value mod 26 (size of alphabet)

    def add(self, key, val):
        if key not in self.keys:
            self.keys.append(key)
            

def main():
    

    pass

if __name__ == "__main__":
    main()