#!/usr/bin/python
from __future__ import print_function
import requests
import sys
import subprocess
import logging

def ticker(currency):
    clist = ['btc','eth','etc','xrp']
    if currency not in clist:
        raise NotImplementedError
    response = requests.get('https://api.coinone.co.kr/ticker/?currency=%s'%(currency))
    contents = response.json()
    return contents['last']

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage : cryptoAlert.py <CurrenyType> <alertValue>')
        print('CurrenyType : btc, eth, etc, xrp')
    else:
        currency = sys.argv[1]
        tvalue = sys.argv[2]
        while 1:
            cvalue = ticker(currency)
            logging.info('Current [ %s ] : %s'%(currency.upper(),cvalue))
            if tvalue <= cvalue:
                logging.warn('Alert! Current [ %s ] is over then %s'%(currency.upper(),tvalue))
                subprocess.Popen('osascript -e \'display notification "Current '+currency.upper()+' : '+cvalue+'" with title "CryptoAlert"\'',shell=True)
