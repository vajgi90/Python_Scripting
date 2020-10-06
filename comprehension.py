#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser(
    description='Search for words including partial word')
parser.add_argument(
    'snippet', help='partial (or complete) string to search for in words')


args = parser.parse_args()
snippet = args.snippet.lower()


with open('/usr/share/dict/words') as f:
    words = f.readlines()


# A longer version can substitue with the solution below
""" 
matches = []
for word in words:
    if snippet in word.lower():
        matches.append(word)
words = open('/usr/share/dict/words').readlines() """

words = open('/usr/share/dict/words').readlines()
print([word.strip() for word in words if snippet in word.lower()])


print(matches)
