### IMPORTS
from bs4 import BeautifulSoup
import requests

def get_thumb(search: str) -> str:
    '''
    Returns the first image for a google search of a given keyword(s)
    '''

    url = f'https://www.google.com/search?q={search}&tbm=isch'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    results = soup.findAll('img')

    try:
        image_url = results[1].get('src')
    except:
        image_url = 'https://i.imgur.com/fCyBeda.jpg'

    return image_url