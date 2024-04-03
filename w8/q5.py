import sys

def main():
    
    # store words
    file1_words = file_to_words(sys.argv[1])
    file2_words = file_to_words(sys.argv[2])

    # print difference
    difference = file1_words - file2_words
    for word in sorted(difference):
        print(word)

def file_to_words(filename):
    words = set()
    # file1 words
    with open(filename) as f1:
        for line in f1:
            line = line.strip()
            words.add(line.lower())
    return words


if __name__ == "__main__":
    main()