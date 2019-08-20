#!/usr/bin/python3

from pprint import pprint
import requests

def main():
    
    with open('/home/student/pyapivz/apikeys/alphavantage.apikey') as apikey:
        myapikey = apikey.read()

    coin = input('Please enter the digital currency for lookup: ') # Allows user to enter the digital currency that they would like to lookup
    coin = coin.upper() # making currency CAPS so that it can be used in f-string URI
    coindata = requests.get(f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={coin}&market=CNY&apikey={myapikey}') #Send HTTP get to the URL with the user input f-string'd
    decodedcoin = coindata.json() # set json output to variable
    currency_name = decodedcoin["Meta Data"]["3. Digital Currency Name"]
    print('----------------------------------------------')
    print(f"Digital Currency selected: {currency_name}")
    print('----------------------------------------------')
    lastrefresh = decodedcoin["Meta Data"]["6. Last Refreshed"] # pulls the last refresh from the meta data section
    lastrefresh = lastrefresh[:-9] # removes the 00:00:00 from the date/time so that it can match the Time Series section
    pprint(decodedcoin["Time Series (Digital Currency Monthly)"][lastrefresh]) # pulls the last refresh date from the json data
            
main()
