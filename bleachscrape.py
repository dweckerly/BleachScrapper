from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def s_get(url):
    try:
        with closing(get(url, stream=True)) as response:
            if is_good_response(response):
                return response.content
            else:
                return None
    except RequestException as e:
        log_error(f'Error during request to {url} : {str(e)}')
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    print(e)

def main():
    raw_html = s_get('http://www.restockit.com/cleaning-supplies/laundry-products/bleach.html')
    html = BeautifulSoup(raw_html, 'html.parser')
    
    div = html.findAll('div', {"class": "rsis_prodname"})
    nameList = []
    for name in div:
        nameList.append(name.text)

    span = html.findAll('span', {"class": "ProdPriceBlack"})
    priceList = []
    for price in span:
        priceList.append(price.text[10:])


main()
