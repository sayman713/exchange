#!/usr/bin/env python3
import requests
import datetime
from datetime import timedelta

# request for cryptocurrency data, via the kraken exchange api

resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD').json()
price = resp['result']['XXBTZUSD']['a'][0][0:5]
oppening_price = resp['result']['XXBTZUSD']['o'][0:5]
temp = open('temp', 'w')

if price > oppening_price:
    print(datetime.datetime.now().strftime(" %d/%m/%Y"), ' BTC/USD ', price, "▲",  file=temp)
else:
    print(datetime.datetime.now().strftime(" %d/%m/%Y"), ' BTC/USD ', price, "▼",  file=temp)

# to output data from the script to the conky config, you need to specify the path to temp,
# for example ${execi 10 cat $HOME/.conky/sayman/temp}

datet = datetime.datetime.now()-timedelta(days=1)
date = datetime.datetime.now()

lincy='http://www.cbr.ru/scripts/XML_daily.asp?date_req='+str(datet.strftime("%d-%m-%Y"))
lincnow='http://www.cbr.ru/scripts/XML_daily.asp?date_req='+str(date.strftime("%d-%m-%Y"))
st = requests.post(lincy).text; sn = requests.post(lincnow).text


def str_num_func(line):
    num_out_of_line = []
    str_num = ""
    for i in range(len(line)):
        if line[i] in "0123456789":
            str_num += line[i]
            try:
                if line[i+1] not in "0123456789":
                    num_out_of_line.append(str_num)
                    str_num = ""
            except:
                num_out_of_line.append(str_num)
    return num_out_of_line


# Currency indices, substitute the desired index, EUR, USD is output by default
#
# GBP[19:21] AZN[14:16] AUD[9:11] INR[69:71] KZT[74:76]
# USD[59:61] AMD[24:26] BYN[29:31] BGN[34:36] BRL[39:41]
# HUF[44:46] HKD[49:51] DKK[54:56] CAD[79:81] KGS[84:86]
# SNY[89:91] MDL[94:96] NOK[99:101] PLN[104:106] RON[109:111]
# EUR[64:66] XDR[114:116] SGD[119:121] TJS[124:126] TRY[129:131]
# TMT[134:136] UZS[139:141] UAH[144:146] CZK[149:151] SEK[154:156]
# CHF[159:161] ZAR[164:166] KRW[169:171] JPY[174:176]


numu1, numu2 = str_num_func(st)[59:61]
numu3 = numu2[0:2]
flusdt = float(numu1+'.'+numu3)

nume1, nume2 = str_num_func(st)[64:66]
nume3 = nume2[0:2]
fleurt = float(nume1+'.'+nume3)

numu1, numu2 = str_num_func(sn)[59:61]
numu3 = numu2[0:2]
flusd = float(numu1+'.'+numu3)

if flusdt <= flusd:
    print(date.strftime(" %d/%m/%Y"), ' USD/RUB ',flusd,'▲', file=temp)
else:
    print(date.strftime(" %d/%m/%Y"), ' USD/RUB ',flusd,'▼', file=temp)


nume1, nume2 = str_num_func(sn)[64:66]
nume3 = nume2[0:2]
fleur = float(nume1+'.'+nume3)

if fleurt <= fleur:
    print(date.strftime(" %d/%m/%Y"), ' EUR/RUB ',fleur,'▲', file=temp)
else:
    print(date.strftime(" %d/%m/%Y"), ' EUR/RUB ',fleur,'▼', file=temp)

temp.close()
exit()
