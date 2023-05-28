import sys


#Given two strings,write a method to decide if one is a permutation of the other.
def checkPermutation1(str1: str, str2: str) -> bool:
    #sort strings and compare
    str1.sort()
    str2.sort()
    return str1 == str2

def checkPermutation2(str1: str, str2: str) -> bool:
    #TODO: is there a more efficient way to do this?
    pass

def main():
    pass
