
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        my_map = str.maketrans("aeiouAEIOU", "AEIOUaeiou")
        print(line.translate(my_map))
        
        # alternate solution
        # line = line.strip()
        # newLine = ""
        # for char in line:
        #     if char in "aeiou":
        #         newLine += char.upper()
        #     elif char in "AEIOU":
        #         newLine += char.lower()
        #     else:
        #         newLine += char
        # print(newLine)


if __name__ == "__main__":
    main()