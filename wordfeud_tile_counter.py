#!/usr/bin/env python
import string
from collections import OrderedDict

START_LETTERS = {
    'A': 10,
    'B': 2,
    'C': 2,
    'D': 5,
    'E': 12,
    'F': 2,	
    'G': 3,	
    'H': 3,	
    'I': 9,	
    'J': 1,	
    'K': 1,	
    'L': 4,	
    'M': 2,
    'N': 6,	
    'O': 7,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 5,
    'T': 7,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1,
}

if __name__ == "__main__":
    with open("letters.txt") as f:
        raw_letters = f.read().strip()

    current_letters = OrderedDict()
    for char in string.ascii_uppercase:
        current_letters[char] = 0

    for l in raw_letters.upper():
        current_letters[l] += 1 

    for l, c in current_letters.iteritems():
        remaining = ''

        if c < START_LETTERS[l]:
            remaining = " (%d)" % (START_LETTERS[l] - c)

        print "%s: %2d %s" % (l, c, remaining)

