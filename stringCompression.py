import sys


# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not 
# become smaller than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z)
def stringCompression(string: str) -> str:
    result = ""
    curr = string[0]
    count = 1
    for i in range(len(string) - 1):
        if curr == string[i+1]:
            count += 1
        else:
            result += curr + str(count)
            curr = string[i+1]
            count = 1
            
        if (i + 1) == (len(string) - 1):
                result += string[i+1] + str(count)

    if len(result) >= len(string):
        result = string

    return result


def main():
    string = sys.argv[1]
    # string = "aabcccccaaa"
    result = stringCompression(string=string)
    print(result)
    return result

if __name__ == "__main__":
    main()