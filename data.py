from parser import pars_description, pars_count_review, pars_data_rating, pars_laptop_price, pars_laptop_name
from bs4 import BeautifulSoup
import requests

base_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

laptops = []

page_number = 0


while True:
    page_number += 1    # adding 1  to parsing information from the all pages
    url = f'{base_url}?page={page_number}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        laptop_elements = soup.find_all('div', class_='card-body')

        if not laptop_elements:
            print(f'No more data on page {page_number}. Exiting loop.')
            break

        for laptop in laptop_elements:
            laptop = str(laptop)
            name = pars_laptop_name(laptop)
            price = pars_laptop_price(laptop)
            description = pars_description(laptop)
            reviews = pars_count_review(laptop)
            rating = pars_data_rating(laptop)

            # create a dictionary with the parsed information

            laptops.append({'name': name, 'price': price, 'description': description,
                            'reviews': reviews, 'rating': rating})
    else:
        print(f'The {url} is wrong. Status code: {response.status_code}')


