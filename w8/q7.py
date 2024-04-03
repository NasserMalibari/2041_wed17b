#!/usr/bin/env python3

import subprocess, re, sys

def main():
    
    process = subprocess.run(f"wget -O- -q {sys.argv[1]}",
                              shell=True, capture_output=True, text=True)
    
    output = process.stdout

    numbers = re.findall(r"[0-9 -]+", output)
    for number in numbers:
        # remove hyphens  and spaces
        number = re.sub("[- ]", "", number)
        
        if len(number) >= 8 and len(number) <= 15:
            print(number)

    # print(numbers[20:30])
    # subprocess.run([wget, -O-, -q, https://www.unsw.edu.au])


if __name__ == "__main__":
    main()