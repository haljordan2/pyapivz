#!/usr/bin/python3

import uuid

ticket = uuid.uuid1()

try:
    print('Type the name of the config file to load onto the switch: ')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileobj:
        switchconfig = configileobj.read()
except Exception as err:
    x = f"There was an issue opening that file: {err}"
else:
    x = f"The file {configfile} was successfully loaded"
finally:
    with open("try12.log", "a") as log:
        print('Writing results to log file')
        print(f"{ticket} - {x}", file=log)

