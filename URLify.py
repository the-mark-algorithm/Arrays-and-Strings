import sys

# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. 
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)

def URLify(string: str, strLen: int) -> str:
    token = "%20"
    result = ""
    words = string.split()
    for i in range(len(words)):
        w = words[i]
        if i == 0:
            result += w
        else:
            result += "%20" + w
    return result


def main():
    string = sys.argv[1]
    strLen = int(sys.argv[2])
    print(URLify(string=string, strLen=strLen))


if __name__ == "__main__":
    main()