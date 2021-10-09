import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='search-results-table')
    cars = catalog.find_all('div', class_='list-item list-label')
    print(cars)
    for car in cars:
        try:
            title = car.find('h2', class_='name').text.strip()
        except:
            title = ''
        try:
            price = car.find('strong').text.strip()
        except:
            price = ''
        try:
            img = car.find('div', class_='thumb-item-carousel').find('img').get('data-src')
        except:
            img = ''
        try:
            des = car.find('p', class_='year-miles').text.strip()
            despa = car.find('p', class_='body-type').text.strip()
            despacito = car.find('p', class_='volume').text.strip()
        except:
            des = ''
            despa = ''
            despacito = ''

        data = {
            'title': title,
            'price': price,
            'img': img,
            'des': des,
            'despa': despa,
            'despacito': despacito
        }

        write_csv(data)

def write_csv(data):
    with open('cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'], data['price'], data['img'], data['des'], data['despa'], data['despacito']))

def main():
    for page in range(1, 856):
        url = f'https://www.mashina.kg/search/all/?page={page}'
        html = get_html(url)
        data = get_data(html)
main()