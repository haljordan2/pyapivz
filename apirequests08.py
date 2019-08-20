#!/usr/bin/python

from pprint import pprint
import requests

def main():
    r = requests.get('https://www.anapioficeandfire.com/api') #Send HTTP get to the URL
    pprint(r.json()) # strip off the json and display on screen

    #r = requests.get('https://www.anapioficeandfire.com/api/books')
    #pprint(r.json())
    
main()


