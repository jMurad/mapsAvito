import requests
import re
import brotli
import time
import json


def get_recaptcha_response(googlekey, page_url):
    url_req = 'http://rucaptcha.com/in.php'
    payload = {'key': '4fd259050808ba3aa49f5d8175675d3b',
               'method': 'userrecaptcha',
               'googlekey': googlekey,
               'pageurl': page_url
               }
    request = requests.get(url_req, proxies='', params=payload)
    captcha_id = request.text.split('|')[1]
    print(request.text)
    url_res = 'http://rucaptcha.com/res.php'
    payload = {'key': '4fd259050808ba3aa49f5d8175675d3b',
               'action': 'get',
               'id': captcha_id
               }
    while 1:
        time.sleep(10)
        response = requests.get(url_res, params=payload)
        print(response.text)
        if response.text != 'CAPCHA_NOT_READY':
            break
    return response.text.split('|')[1]

url = 'https://www.avito.ru/dagestan#login?s=h'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'
                      '3.86 Safari/537.36',
        'referer': f'{url}',
        'accept-encoding': 'gzip, deflate, br',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://www.avito.ru',
        'cookie':   'u=2fdwrhq0.1dgwiyw.g0ebt8t2kn;'
                    '_ga=GA1.2.787839117.1550752754;'
                    '_fbp=fb.1.1550752754027.1309230693;'
                    '_ym_uid=1550752754172788459;'
                    '_ym_d=1550752754;'
                    '__gads=ID=aa4f41e1d4691557:T=1550752948:S=ALNI_MbcuKzt-jMpK82KekqS44Rvyw3YgQ;'
                    'buyer_location_id=646710;'
                    '__utmz=99926606.1551856488.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);'
                    'cto_lwid=331c2981-71ff-4c18-91b9-32e42a394852;'
                    'buyer_selected_search_radius4=0_general;'
                    'rheftjdd=rheftjddVal;'
                    'buyer_tooltip_location=0;'
                    '__utma=99926606.787839117.1550752754.1555507406.1556515479.3;'
                    '__utmc=99926606;'
                    'weborama-viewed=1;'
                    'f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e0'
                        '6cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e0'
                        '8b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a0df103df0c26013ae2bfa4611a'
                        'ac769efa4d7ea84258c63d74c4a16376f87ccd897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9'
                        'ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19d'
                        'a9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba'
                        '923b7b327da7e87a84e371fc60d21abab15028c5344d5e61d702b2ac73f74e18fe67f83c251a220b07340691ed2c86'
                        '977b8878fcf22eb98f05791aec91c58732de926882853a9d9b2ff8011cc827c4d07ec9665f0b70915ac1de0d034112'
                        '7bf595591ec453710bfe55200d50a76b2da10fb74cac1eab2da10fb74cac1eab252b714e325703fcf3f6f32573380e'
                        'cd517083b9c0063862;'
                    '_gid=GA1.2.1517368967.1556515979;'
                    '_ym_isad=2;'
                    '_nfh=2face4e4a88cd0abbf178edb1f17dd17;'
                    'crto_uid=97a7dde2fb1d8908a1f556470b3e332c;'
                    'anid=removed;'
                    'sessid=03ea0023162507da7358abc483817f96.1556525078;'
                    'v=1556534026;'
                    'dfp_group=14;'
                    'abp=0;'
                    '_ym_visorc_34241905=b;'
                    'buyer_from_page=main',
        'content-type': 'application/json; charset=UTF-8',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8'
}
s = requests.Session()
r = s.get(url, headers='', proxies='')
# print(r.cookies['sessid'] + '\n' + r.cookies['v'])
# print(r.headers['Set-Cookie'])
# print(r.headers['Set-Cookie'].split(';')[0])
# print(r.headers['Set-Cookie'].split(';')[7].split(',')[1])
# print(r.headers['Set-Cookie'].split(';')[33].split(',')[1])
j = json.loads('{'+r.headers['Set-Cookie']+'}')
print(j['sessid'])
html = r.text

'''
# jstoken[1] - token[###] and jstoken[2] - ####
jstoken = re.search(r'name="token\[([\d]+?)\]"\s+value="([\w\d]+?)"', html)
googlekey = '6LekaEcUAAAAAHeBEnl8an4WEF2J8pSHZDebFTBZ'
g_recaptcha_response = get_recaptcha_response(googlekey, url)
data = {'login': 'deit91@yandex.ru',
        'password': 'M3244dmk',
        'remember': 'true',
        f'token[{jstoken[1]}]': jstoken[2],
        'g-recaptcha-response': g_recaptcha_response
        }
url_login = 'https://www.avito.ru/auth/login'
r = s.post(url_login, headers=headers, data=data)
'''