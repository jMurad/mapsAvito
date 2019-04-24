import requests
from bs4 import BeautifulSoup
from re import findall
import datetime
from PIL import Image
from io import StringIO, BytesIO
import base64
import time


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer': f'{url}',
        'accept-encoding': 'gzip, deflate, br',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://www.avito.ru',
        'cookie': 'u=2fdwrhq0.1dgwiyw.g0ebt8t2kn; _ga=GA1.2.787839117.1550752754; _fbp=fb.1.1550752754027.1309230693; _ym_uid=1550752754172788459; _ym_d=1550752754; __gads=ID=aa4f41e1d4691557:T=1550752948:S=ALNI_MbcuKzt-jMpK82KekqS44Rvyw3YgQ; buyer_location_id=646710; __utma=99926606.787839117.1550752754.1551856488.1551856488.1; __utmz=99926606.1551856488.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cto_lwid=331c2981-71ff-4c18-91b9-32e42a394852; buyer_tooltip_location=646710; verified_badge_closed=1; buyer_selected_search_radius4=0_general; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a0df103df0c26013ae2bfa4611aac769efa4d7ea84258c63d74c4a16376f87ccd897baa7410138eadfb0fb526bb39450a46b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da7e87a84e371fc60d21abab15028c5344d5e61d702b2ac73f74e18fe67f83c251a220b07340691ed2c86977b8878fcf22eb98f05791aec91c58732de926882853a9d9b2ff8011cc827c4d07ec9665f0b70915ac1de0d034112bf7943cc5ed42f50a7dd0b023ca127dd2da10fb74cac1eab2da10fb74cac1eab252b714e325703fcf3f6f32573380ecd517083b9c0063862; sessid=0aac75a4ba0abfa11588601adefa83a7.1554462922; v=1554462922; dfp_group=14; rheftjdd=rheftjddVal; _ym_isad=2; _ym_visorc_34241905=b; _gid=GA1.2.1170361078.1554463146; _ym_visorc_45148551=w; _dc_gtm_UA-2546784-1=1; sx=H4sIAAAAAAACAxXFUQqAIAwA0Lvsuw%2BTrcTbxFKLgQZGQ8S7V%2FDgdeBY1a65hawsRlVSKSzqKvgOD3hYttzOez%2BuqIVRJDlk9%2Bc%2BRmCCAH4mQiJjLI7xAqB1j55UAAAA; abp=0',
        'content-type': 'application/json; charset=UTF-8',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8'
    }
    s = requests.Session()
    r = s.get(url, headers=headers)
    #r = requests.get(url)
    print(r)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page = soup.find('div', class_='pagination-pages')
    pages = page.find_all('a', class_='pagination-page')[-1]['href']
    total_pages = pages.split('=')[1].split('&')[0]
    print('Количество страниц: ' + total_pages)
    return int(total_pages)


def get_all_pages(url):
    total_pages = get_total_pages(get_html(url))
    base_url = 'https://www.avito.ru/dagestan/telefony?'
    page_part = 'p='
    item_name = url.split('=')[2]
    query_part = f'&q={item_name}'
    url_gen = []
    for i in range(1,total_pages+1):
        url_gen.append(base_url + page_part + str(i) + query_part)
    return url_gen


def strtodate(strn):
    date_var = datetime.date
    if strn.lower() == 'сегодня':
        date_var = datetime.date.today()
    elif strn.lower() == 'вчера':
        date_var = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
    else:
        month = ['янв','фев','мар','апр','май','июн','июл','авг','сен','окт','ноя','дек']
        i = 0
        for mn in month:
            i += 1
            if mn in strn.split(' ')[1].lower():
                date_var = datetime.date(2019, i, int(strn.split(' ')[0]))
                break
    date = str(date_var)
    return date


def get_image_pkey(ad_id, ad_phone):
    if ad_id and ad_phone:
        ad_subhash = findall(r'[0-9a-f]+', ad_phone)
        if int(ad_id) % 2 == 0:
            ad_subhash.reverse()
        ad_subhash = ''.join(ad_subhash)
        return ad_subhash[::3]


def get_all_advert(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find_all('div', class_='item_table')
    print('Количество объявлений на странице: ', len(ads))
    ad= []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer': f'{url}',
        'accept-encoding': 'gzip, deflate, br'
    }
    s = requests.Session()
    for i in range(30,31):
        time.sleep(5)
        every_ad = ads[i]
        soup2 = BeautifulSoup(str(every_ad), 'lxml')
        link = soup2.find('a', class_='item-description-title-link')['href']
        data_raw = soup2.find('div', class_='js-item-date')['data-absolute-date']
        data_str = str(data_raw).split('\xa0')[0].strip()
        data = strtodate(data_str)
        data_item_id = every_ad['data-item-id']
        data_pkey = every_ad['data-pkey']
        pkey = get_image_pkey(data_item_id, data_pkey)
        image = s.get(f'http://www.avito.ru/items/phone/{data_item_id}?pkey={pkey}', headers=headers).json().get('image64')
        if image:
            base64_image = image.split(',')[1]
            phone = recognize(base64_image)
        else:
            phone = '88888888888'
        ad.append({'id': data_item_id, 'link': link, 'date': data, 'phone': phone})
    return ad


def recognize(base64_image):
    image = Image.open(BytesIO(base64.b64decode(base64_image))).convert('LA')
    left_margins = (5, 39, 63, 86, 122, 146, 169, 207, 231, 268, 292)
    DIGITS_BY_HIST = {358: '0', 162: '1', 331: '2', 328: '3', 285: '4', 336: '5', 396: '6', 216: '7', 403: '8',
                      383: '9'}
    digits = []
    for index, left_margin in enumerate(left_margins, start=1):
        box = (left_margin, 13, left_margin + 21, 13 + 31)
        digit = image.crop(box)
        characteristic = digit.histogram()[0]
        digits.append(DIGITS_BY_HIST.get(characteristic, 'x'))
    return ''.join(digits)


def main():
    url = 'https://www.avito.ru/dagestan/telefony?s=104&p=1&q=samsung'
    all_pages = get_all_pages(url)
    page_url = all_pages[0]
    ads = get_all_advert(page_url)
    for ad in ads:
        print('\n' + ad['link'] + '\n' + ad['date'] + '\n' + ad['phone'] + '\n')


'''
        strn = []
        i = 0
        i += 1
        if i > 10:
            break
        print(f'http://www.avito.ru/items/phone/{ad["data_item_id"]}?pkey={ad["pkey"]}')
        strn.append(f'http://www.avito.ru/items/phone/{ad["data_item_id"]}?pkey={ad["pkey"]}')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer': f'{url}',
        'accept-encoding': 'gzip, deflate, br'
    }
    s = requests.Session()
    for st in strn:
        #image = s.get(st, headers=headers).json().get('image64')
        image = s.get(st, headers=headers)
        image = image.json()
        image = image.get('image64')
        if image:
            base64_image = image.split(',')[1]
            phone = recognize(base64_image)
            print(phone)
'''


if __name__ == '__main__':
    main()
