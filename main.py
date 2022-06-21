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

tccurl = 'https://www.tccb.gov.tr/'
prompturl = tccurl + 'receptayyiperdogan/konusmalar/?&page=1'
headers = {'User-Agent': 'my user agent(google)'}
request = requests.get(prompturl, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')
prompt_div = soup.find('div', id='divContentList')
a_s = prompt_div.find_all('a')

urlList = []
dic = {}
for a in a_s:
    url = a.get('href')
    subject = a.text
    url = tccurl + url
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    speech = soup.find('div', id='divContentArea').text.replace('\n', '').replace('.', ' ').replace(',', ' ')\
        .replace('?', ' ').replace('!', ' ').replace(':', ' ').replace(';', ' ').replace("'", " ").lower()
    urlList.append([subject, speech])
    wordCount(speech, dic)

df = pd.DataFrame(data=orderDict(dic), columns=['Word', 'Count'])
saveAsExcel(df)

