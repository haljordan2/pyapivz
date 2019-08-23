#!/usr/bin/python

import re

def regex_example():
    with open('requirements.txt') as req:
        for x in req:
            mymatch = re.search('^[su].*$', x)
            if mymatch:
                print(mymatch.group())

regex_example()
