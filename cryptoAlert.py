#!/usr/bin/python
from __future__ import print_function
import requests
import sys
import subprocess
import logging

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
    if len(sys.argv) > 4:
        print('usage : cryptoAlert.py <CurrenyType> <alertOverValue> <alertUnderValue>')
        print('CurrenyType : btc, eth, etc, xrp')
    else:
        currency = sys.argv[1]
        tovalue = sys.argv[2]
        cnt = 0
		term = 10
        if len(sys.argv) == 4:
            tuvalue = sys.argv[3]
        else:
            tuvalue = 0
        while 1:
            cvalue = ticker(currency)
            logging.info('Current [ %s ] : %s'%(currency.upper(),cvalue))
            if tovalue <= cvalue:
                logging.warn('Alert! Current [ %s ] is over then %s'%(currency.upper(), tovalue))
				if cnt == term:
					alert('Alert! Current [ %s / %s ] is over then %s'%(currency.upper(), cvalue, tovalue))
					cnt = 0
				cnt += 1
            if tuvalue >= cvalue:
                logging.warn('WARNING! Current [ %s ] is under then %s'%(currency.upper(), tuvalue))
                if cnt == term:
                    alert('WARNING! Current [ %s / %s ] is under then %s'%(currency.upper(), cvalue, tuvalue))
                    cnt = 0 
                cnt += 1
