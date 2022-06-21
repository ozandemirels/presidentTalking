import time

import requests
from bs4 import BeautifulSoup
import pandas as pd


def wordCount(str, counts):
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def orderDict(str):
    d_sorted_by_value = sorted(str.items(), key=lambda x: x[1], reverse=True)
    return d_sorted_by_value

def saveAsExcel(df):
    df.to_excel("C:/Users/ozan.demirel/Desktop/thisIsPresidentTalking.xlsx")


dic = {}
forStatus = ''
for i in range(1,999):
    tccurl = 'https://www.tccb.gov.tr/'
    prompturl = tccurl + 'receptayyiperdogan/konusmalar/?&page=' + str(i)
    headers = {'User-Agent': 'my user agent(google)'}
    request = requests.get(prompturl, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    prompt_div = soup.find('div', id='divContentList')
    dls = prompt_div.find_all('dl')

    for dl in dls:
        date = dl.dt.text
        if date[6:10] == '2022':
            subject = dl.dd.a.text
            url = dl.dd.a.get('href')
            url = tccurl + url
            request = requests.get(url, headers=headers)
            soup = BeautifulSoup(request.content, 'html.parser')
            speech = soup.find('div', id='divContentArea').text.replace('\n', '').replace('.', ' ').replace(',', ' ')\
                .replace('?', ' ').replace('!', ' ').replace(':', ' ').replace(';', ' ').replace('"', '')\
                .replace("'", "").replace("'", "").replace("-", " ").lower()
            wordCount(speech, dic)
        elif date[6:10] != '2022':
            forStatus = 'Exit'
            break
    print(len(dic))
    if forStatus == 'Exit':
        break

df = pd.DataFrame(data=orderDict(dic), columns=['Word', 'Count'])
saveAsExcel(df)

