
import glob

def main():
    c_files = glob.glob("*.[ch]")

    total = 0
    for c_file in c_files:
        with open(c_file) as f:
            # get number of lines
            num_lines = len(f.readlines())
            total += num_lines
            print(f"{num_lines:>7} {c_file}")
            # print(num_lines)
    print(f"{total:>7} total")
if __name__ == "__main__":
    main()