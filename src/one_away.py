from collections import defaultdict
import sys

# There are three types of edits that can be performed on strings: 
#   1. insert a character 
#   2. remove a character 
#   3. or replace a character
#  
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def oneAway(s1: str, s2: str) -> bool:
    s1 = ''.join(s1.split()).lower()
    s2 = ''.join(s2.split()).lower()
    
    # create map for the counting character multiplicities
    multiplicities = defaultdict(int)

    for char in s1:
        multiplicities[char] += 1
    
    for char in s2:
        multiplicities[char] -= 1
        
    return abs(sum(multiplicities.values())) <= 1

def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    result = oneAway(s1=s1, s2=s2)
    print(result)
    return result

if __name__ == "__main__":
    main()