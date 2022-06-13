import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import date
import time

url = 'https://www.tccb.gov.tr/receptayyiperdogan/konusmalar/?&page=1'

headers = {'User-Agent': 'my user agent(google)'}
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')
prompt_div = soup.find('div', id='divContentList')
dls = prompt_div.find_all('dl')

for dl in dls:
    print(dl.text)

#home_divs.dl[0].text




time.sleep(55)






for home_div in home_divs:
    home_price = home_div.find('div', class_='list-view-price').text.strip('TL').strip('EUR').strip('USD').strip()
    home_price_currency = home_div.find('span', class_='currency').text.strip()
    home_date = home_div.find('div', class_='list-view-date').text.strip()
    home_type = home_div.find('div', class_='left').text
    home_type = home_type[0:home_type.index(' ') - 1]
    home_numberofroom = home_div.find('span', class_='celly houseRoomCount').text.replace(' ', '')
    home_size = home_div.find('span', class_='celly squareMeter list-view-size').text.replace(' ', '').strip(' ')
    home_size = home_size[1:home_size.index('m') + 2]
    home_neighbourhood = home_div.find('div', class_='list-view-location').text.replace(' ', '')
    home_neighbourhood = home_neighbourhood[1:home_neighbourhood.index(',')]

    house_list.append([home_price, home_price_currency, home_date, home_type, home_numberofroom, home_size,home_neighbourhood])
page += 1
print(str(page) + '. sayfaya geçiliyor')






workbook = Workbook()
sheet = workbook.active

for row in house_list:
    sheet.append(row)

today = str(date.today())
workbook.save(filename="C:/Users/ozan.demirel/Desktop/House_Prices/house_infos_in_izmir_" + today + ".xlsx")



