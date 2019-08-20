#!/usr/bin/python3

def main():
    with open('datacenter.json', 'r') as datacenter:
        datacenterstr = datacenter.read()

    print(type(datacenterstr))
    datacenterdict = json.loads(datacenterstr)
    print(type(datacenterdict))
    print(datacenterdect['row1'])

    with open('datacenter.json', 'r') as datacenter:
        datacentershort = json.load(datacenter)
    print(type(datacentershort))

main()
