from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def s_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
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

    create_outfile(nameList, priceList)
    

def create_outfile(nameList, priceList):
    file = open('bleachPrices.txt', 'w+')
    for i in range(len(priceList)):
        file.write(f'{nameList[i]} - {priceList[i]}\n')

main()