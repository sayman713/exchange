#!/usr/bin/env python3
import requests; import datetime
from datetime import timedelta

# для вывода данных из скрипта в конфиг conky, необходимо прописать путь до temp,
# к примеру ${execi 10 cat $HOME/.conky/sayman/temp}

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


# Индексы валют, подставьте нужный индекс, по умолчанию выведено EUR, USD
# GBP[19:21] AZN[14:16] AUD[9:11] INR[69:71] KZT[74:76]
# USD[59:61] AMD[24:26] BYN[29:31] BGN[34:36] BRL[39:41]
# HUF[44:46] HKD[49:51] DKK[54:56] CAD[79:81] KGS[84:86]
# SNY[89:91] MDL[94:96] NOK[99:101] PLN[104:106] RON[109:111]
# EUR[64:66] XDR[114:116] SGD[119:121] TJS[124:126] TRY[129:131]
# TMT[134:136] UZS[139:141] UAH[144:146] CZK[149:151] SEK[154:156]
# CHF[159:161] ZAR[164:166] KRW[169:171] JPY[174:176]


numu1, numu2 = str_num_func(st)[59:61]; flusdt = float(numu1+'.'+numu2)
nume1, nume2 = str_num_func(st)[64:66]; fleurt = float(nume1+'.'+nume2)


temp = open('temp', 'w')

numu1, numu2 = str_num_func(sn)[59:61]; flusd = float(numu1+'.'+numu2)
if flusdt <= flusd:
    print(date.strftime(" %d/%m/%Y"), ' USD ',flusd,' ▲', file=temp)
else:
    print(date.strftime(" %d/%m/%Y"), ' USD ',flusd,' ▼', file=temp)


nume1, nume2 = str_num_func(sn)[64:66]; fleur = float(nume1+'.'+nume2)
if fleurt <= fleur:
    print(date.strftime(" %d/%m/%Y"), ' EUR ',fleur,' ▲', file=temp)
else:
    print(date.strftime(" %d/%m/%Y"), ' EUR ',fleur,' ▼', file=temp)

temp.close()

