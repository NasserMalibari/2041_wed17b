#! /usr/bin/env python3

import re, subprocess
from collections import Counter
from argparse import ArgumentParser


def hello():
    print('hello')


def main():

    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    process = subprocess.run(["wget", "-q", "-O-", args.url],
                             capture_output=True, text=True)
    
    output = process.stdout.lower()

    tags = re.findall('<\s*(\w+)', output)

    tags_counter = Counter(tags)

    if args.frequency:
        # print in numeric order
        for tag, count in tags_counter.most_common():
            print(f"{tag} {count}")
    else:
        for tag, count in sorted(tags_counter.items()):
            print(f"{tag} {count}")

if __name__ == "__main__":
    main()
