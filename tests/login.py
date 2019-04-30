import requests
import re
import brotli
import time
import json
from python_rucaptcha import ReCaptchaV2, RuCaptchaControl, CallbackClient


def format_headers(url_, u_, sessid_, v_, dfp_group_):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.368'
                      '3.86 Safari/537.36',
        'referer': f'{url_}',
        'accept-encoding': 'gzip, deflate, br',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://www.avito.ru',
        'cookie': f'u={u_};'
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
                  f'sessid={sessid_};'
                  f'v={v_};'
                  f'dfp_group={dfp_group_};'
                  'abp=0;'
                  '_ym_visorc_34241905=b;'
                  'buyer_from_page=main',
        'content-type': 'application/json; charset=UTF-8',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8'
    }
    return headers


def get_recaptcha_response(googlekey, page_url):
    url_req = 'http://rucaptcha.com/in.php'
    payload = {'key': 'b6db28046b6e4788f65cb763e648dc27',
               'method': 'userrecaptcha',
               'googlekey': googlekey,
               'pageurl': page_url,
               'proxy': 'user24145:eshj54@5.188.72.179:6676',
               'proxytype': 'HTTPS',
               'debug_dump': 1
               }
    # b6db28046b6e4788f65cb763e648dc27
    print('recaptcha:', googlekey, page_url)
    request = requests.get(url_req, params=payload)
    print(request.text)
    captcha_id = request.text.split('|')[1]
    print(captcha_id)
    url_res = 'http://rucaptcha.com/res.php'
    payload = {'key': 'b6db28046b6e4788f65cb763e648dc27',
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


def rucaptcha(googlekey, url):
    RUCAPTCHA_KEY = "b6db28046b6e4788f65cb763e648dc27"
    # Google sitekey
    SITE_KEY = googlekey
    # ссылка на страницу с капчёй
    PAGE_URL = url

    # Пример работы с модулем ReCaptchaV2
    answer_usual_re2 = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(
        site_key=SITE_KEY, page_url=PAGE_URL
    )
    print(answer_usual_re2['captchaSolve'])
    return answer_usual_re2['captchaSolve']


headers = format_headers('https://www.avito.ru/dagestan', '2fhd5y1k.1dgwiyw.g2koc2mbwu',
                              '4990f9e889e44bd5fd27235af560fb83.1556607992', '1556607992', '30')
proxies = {'http': 'http://user24145:eshj54@5.188.72.179:6676'}
url_login = 'https://www.avito.ru/auth/login'
url = 'https://www.avito.ru/dagestan'
s = requests.Session()
r = s.get(url, headers=headers, proxies=proxies)
print(r.headers['Set-Cookie'])
v = r.cookies['v']
sessid = r.headers['Set-Cookie'].split(';')[0].split('=')[1]
u = r.headers['Set-Cookie'].split(';')[7].split(', ')[1].split('=')[1]
# dfp_group = r.headers['Set-Cookie'].split(';')[33].split(', ')[1].split('=')[1]
print('v', v)
print('sessid', sessid)
print('u', u)
# print('dfp_group', dfp_group)
jstoken = re.search(r'name="token\[([\d]+?)\]"\s+value="([\w\d]+?)"', r.text)
googlekey = '6LekaEcUAAAAAHeBEnl8an4WEF2J8pSHZDebFTBZ'
g_recaptcha_response = get_recaptcha_response(googlekey, url+'#login?s=h')
html = r.text
data = {'login': 'deit91@yandex.ru',
        'password': 'M3244dmk',
        'remember': 'true',
        f'token[{jstoken[1]}]': jstoken[2],
        'g-recaptcha-response': g_recaptcha_response
        }
headers = format_headers(url, u, sessid, v, '30')
r = s.post(url_login, headers=headers, proxies=proxies, data=data)
print(r.text)
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