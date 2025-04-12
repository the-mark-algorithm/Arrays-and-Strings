from collections import defaultdict
import sys

#Given two strings,write a method to decide if one is a permutation of the other.
def checkPermutation1(str1: str, str2: str) -> bool:
    str1 = str1.lower()
    str2 = str2.lower()

    #sort strings and compare
    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))

    return str1 == str2

def checkPermutation2(str1: str, str2: str) -> bool:
    #TODO: is there a more efficient way to do this?

    # First check if both strings are same length
    if (len(str1) != len(str2)):
        return False
    
    str1 = str1.lower()
    str2 = str2.lower()

    # Use Hash table / defaultdict
    letters1 = defaultdict(int)


    for i in range(len(str1)):
        letters1[str1[i]] += 1

    for i in range(len(str2)):
        if (letters1[str2[i]] > 0):
            letters1[str2[i]] -= 1
        else:
            return False
        
    return True

def main():
    # argv = [ checkPermutation.py ]
    string1 = input("Enter First Word: ")
    string2 = input("Enter Second Word: ")

    result = checkPermutation2(string1, string2)

    print("First word: ", string1)
    print("Second word:", string2)
    print("Are they a permutation of each other?: ", result)

    return result

if __name__ == "__main__":
    main()