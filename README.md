# CryptoAlert
영차영차
<br>
![noti](https://raw.githubusercontent.com/0xsaika/CryptoAlert/master/image.png)
<br>
목표시세를 넘어가거나 설정한 시세보다 낮아지면 terminal을 통해 notify를 띄워줍니다
더이상귀찮게 매번 차트를 보지마세요! 빵긋
```
usage : cryptoAlert.py <CurrenyType> <alertOverValue> <alertUnderValue>
CurrenyType : btc, eth, etc, xrp
```
## Info
 - using Coinone API
 - for OSX
    - ```osascript -e 'display notification "Current %s : %s" with title "CryptoAlert"'```
 - It work on my computer :)
