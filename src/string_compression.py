import sys


# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not 
# become smaller than the original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z)
def string_compression(string: str) -> str:
    result = ""
    count = 0

    if len(string) <= 2:
        return string

    for i in range(len(string) - 1):
        curr = string[i]
        next = string[i+1]

        count += 1

        if curr != next:
            result += curr + str(count)
            count = 0
        
        if i >= len(string) - 2:
            result += next + str(count + 1)

    if len(result) >= len(string):
        result = string

    return result


def main():
    string = sys.argv[1]
    # string = "aabcccccaaa"
    result = string_compression(string=string)
    print(result)
    return result

if __name__ == "__main__":
    main()