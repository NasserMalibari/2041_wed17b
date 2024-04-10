#! /usr/bin/env python3

from collections import Counter
from argparse import ArgumentParser
import q3
import requests
from bs4 import BeautifulSoup

def main():

    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    response = requests.get(args.url)
    webpage = response.text.lower()

    # print(webpage)
    soup = BeautifulSoup(webpage, 'html.parser')

    # print(soup.prettify())
    
    # soup = BeautifulSoup(webpage, 'html5lib')

    tags = soup.find_all()

    # tag_names = []
    # for tag in tags:
    #     tag_names.append(tag.name)
    
    tag_names = [ tag.name for tag in tags ]

    tags_counter = Counter(tag_names)

    if args.frequency:
        # print in numeric order
        for tag, count in tags_counter.most_common():
            print(f"{tag} {count}")
    else:
        for tag, count in sorted(tags_counter.items()):
            print(f"{tag} {count}")

if __name__ == "__main__":
    # main()
    q3.hello()