#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name": "zaphod beeblebrox", "species": "betelguesian"}, {"name": "author dent", "species": "human"}, {"name": "ford prefict", "species": None}]
    
    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

    myhitchhikers = json.dumps(hitchhikers)

    print(myhitchhikers)

main()
