from collections import defaultdict
from checkPermutation import checkPermutation1
import sys

# Given a string, write a function to check if it is a permutation of a palin­ drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def isPalindromePermutation(string: str) -> bool:
    # for a string a string to be a permutation of a palindrome 1 must be true:
    #(1) if string has even number of letters, there must be a multiple of 2 of each letter (0,2,4,6...)
    #(2) if string has odd number of letters, there must be 1 unique letter (middle letter) and the rest must come in pairs

    # remove all whitespace, set to lower case and sort
    string = ''.join(string.split()).lower()
    alphabet = defaultdict(int)
    for s in string:
        alphabet[s] += 1

    if (len(string) % 2 == 0):
        for key in alphabet.keys():
            if (alphabet[key] % 2 != 0):
                return False
    if (len(string) % 2 != 0):
        foundUnique = False
        for key in alphabet.keys():
            if alphabet[key] % 2 != 0:
                if alphabet[key] == 1 and not foundUnique:
                    foundUnique = True
                    continue
                else:
                    return False
    return True

def main():
    string = sys.argv[1]
    print(isPalindromePermutation(string=string))

if __name__ == "__main__":
    main()