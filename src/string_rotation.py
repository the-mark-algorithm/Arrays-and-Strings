# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
# (e.g.,"waterbottle" is a rotation of"erbottlewat").

def is_substring(s1, s2):
    idx1 = 0
    idx2 = 0

    if len(s1) != len(s2):
        return False

    while s1[idx1] != s2[idx2]:
        idx2 += 1
        
        if idx2 == len(s2):
            return False
        
    
    while idx1 < len(s1):
        if s1[idx1] != s2[idx2]:
            return False
        
        idx1 += 1
        idx2 = (idx2 + 1) % len(s2)
    
    return True


def main():
    s1 = input("Enter the first word: ").strip()
    s2 = input("Enter the second word: ").strip()

    print("First Word: ", s1)
    print("Second Word: ", s2)

    result = is_substring(s1, s2)

    print("Is substring? ", result)

if __name__ == "__main__":
    main()




        
