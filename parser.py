import traceback
from bs4 import BeautifulSoup


def pars_laptop_name(html_text: str):      # parsing laptop name
    if html_text is None:
        return None
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.find('a', class_='title').next_element
    except Exception as exp:
        print("text from html err", exp)
        traceback.print_exc()
        return ''


def pars_laptop_price(html_text: str):   # parsing  laptop price
    if html_text is None:
        return None
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.find('div', class_='caption').find('h4').next_element
    except Exception as exp:
        print("text from html err", exp)
        traceback.print_exc()
        return ''


def pars_description(html_text: str):   # parsing tech information about laptop
    if html_text is None:
        return None
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.find('p', class_='description card-text').next_element
    except Exception as exp:
        print("text from html err", exp)
        traceback.print_exc()
        return ''


def pars_count_review(html_text: str):   # parsing quantity of reviews
    if html_text is None:
        return None
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.find('p', class_='review-count').next_element
    except Exception as exp:
        print("text from html err", exp)
        traceback.print_exc()
        return ''


def pars_data_rating(html_text: str):   # parsing rating
    if html_text is None:
        return None
    try:
        soup = BeautifulSoup(html_text, 'html.parser')
        rating_element = soup.find('p', {'data-rating': True})
        return rating_element['data-rating']
    except Exception as exp:
        print("text from html err", exp)
        traceback.print_exc()
        return ''
