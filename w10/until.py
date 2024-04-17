#!/usr/bin/env python3

import sys, re

def line_matches(address, line, line_num):
    """
        address: str [either a number or /<regex>/]
    """
    if re.fullmatch(r"\d+", address):
        return line_num == int(address)
    elif re.fullmatch(r"/.*/",  address):
        # get regex part
        regex = address[1:-1]
        return (re.search(regex, line)) != None
    else:
        raise ValueError("i dont know this address type")
    return False

def main():
    pass
    # /.3/ OR 3
    address = sys.argv[1]

    for line_num, line in enumerate(sys.stdin, start=1):
        # remove last char if its a newline
        if len(line) > 0 and line[-1] == "\n":
            line = line[0:-1]

        print(line)
        if line_matches(address, line, line_num):
            sys.exit(0)


if __name__ == "__main__":
    main()