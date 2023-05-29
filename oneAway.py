from collections import defaultdict
import sys


# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def oneAway(s1: str, s2: str) -> bool:
    s1 = ''.join(s1.split()).lower()
    s2 = ''.join(s2.split()).lower()
    numAway = 0
    
    # create hash map for the shorter string
    hashmap = defaultdict(int)
    if len(s1) <= len(s2):
        target1 = s1
        target2 = s2
    else:
        target1 = s2
        target2 = s1

    for char in target1:
        hashmap[char] += 1
    
    for char in target2:
        if hashmap[char] == 0:
            numAway += 1
        
    return numAway <= 1

def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    result = oneAway(s1=s1, s2=s2)
    print(result)
    return result

if __name__ == "__main__":
    main()