import requests
from bs4 import BeautifulSoup
import datetime
import re
import brotli
from requests.auth import HTTPProxyAuth


def get_html(url):
    proxies = {'https': 'http://yahyaevml:Murad353694@172.19.96.51:9090'}
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
    r = s.get(url, headers=headers, proxies=proxies)
    # print('0:', requests.utils.dict_from_cookiejar(r.cookies))
    # print('1:', r.headers)
    return [r.text, r.content]


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1]['href']
    total_pages = pages.split('=')[1].split('&')[0]
    print(total_pages)
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
    if strn.lower() == 'сегодня':
        date = datetime.date.today()
    elif strn.lower() == 'вчера':
        date = datetime.date.today() - 1
    return date


def get_all_advert(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find_all('div', class_='item_table')
    ad = []

    for every_ad in ads:
        soup2 = BeautifulSoup(str(every_ad), 'lxml')
        link = soup2.find('a', class_='item-description-title-link')['href']
        data_raw = soup2.find('div', class_='js-item-date')['data-absolute-date']
        data_str = str(data_raw).split('\xa0')[0].strip()
        data = datetime.strptime(data_str)
        ad.append({'link': link, 'data': data})

    return ad


def main():
    url = 'https://www.avito.ru/dagestan#login?s=h'
    html = get_html(url)[0]
    # soup = BeautifulSoup(html, 'lxml')

    # page = soup.findall('script', src=re.compile(r"https://www.avito.st/s/cc/chunks/.*"))
    page = re.findall(r'src="(https://www.avito.st/s/cc/chunks/.*?)"', html)
    i = 0
    for pg in page:
        i += 1
        htm = get_html(pg)
        decompressed_data = str((brotli.decompress(htm[1])).decode('utf-8'))
        # res = re.findall(r'c=t\?(".+?");', htm)
        res = re.findall(r'c=t\?(".+?");', decompressed_data)
        print("------------------------------")
        print(pg)
        print(res)
    # pages = page.find_all('a', class_='pagination-page')[-1]['href']

    # pages = soup.find('div', class_='grecaptcha-logo') # .find_all('iframe', name_='a-cac0m9fpvasg')[-1]['href']
    # total_pages = pages.split('=')[1].split('&')[0]
    # file = open('content.html', 'w', encoding='utf-8')
    # file.write(html)
    # file.close()



if __name__ == '__main__':
    main()

