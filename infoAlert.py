#!/usr/bin/python
from __future__ import print_function
import requests
import sys
import subprocess
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('saika')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter('[%(levelname)s|%(asctime)s > %(message)s'))
logger.addHandler(streamHandler)

def ticker(currency):
    clist = ['btc','eth','etc','xrp']
    if currency not in clist:
        raise NotImplementedError
    response = requests.get('https://api.coinone.co.kr/ticker/?currency=%s'%(currency))
    contents = response.json()
    return contents['last']

def alert(description):
    subprocess.Popen('osascript -e \'display notification "'+description+'" with title "CryptoAlert"\'',shell=True)

if __name__ == "__main__":
        while 1:
            ETH = ticker('eth')
            XRP = ticker('xrp')
            log = 'ETH : %s\nXRP : %s'%(ETH,XRP)
            print(log)
            alert(log)
            time.sleep(3)
