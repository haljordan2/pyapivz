#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "zaphod beeblebrox", "species": "betelguesian"}, {"name": "author dent", "species": "human"}, {"name": "ford prefict", "species": None}]
    
    with open("zfile.yml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)
         
         

main()
