import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='list-view')
    mobiles = catalog.find_all('div', class_='item product_listbox oh')
    for mobile in mobiles:
        try:
            image = mobile.find('img').get('src')
            print(type(image))
        except:
            image = ''
        try:
            title = mobile.find('div', class_='listbox_title oh').text
        except:
            title = ''
        try:
            price = mobile.find('div', class_='listbox_price text-center').text
        except:
            price = ''

        data = {
            'title': title,
            'image': image,
            'price': price
        }

        write_csv(data)

def write_csv(data):
    with open ('mobiles.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['image'], data['price']))

def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(url)
    get_data(html)

main()