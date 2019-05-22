import requests


LOGIN_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Referer': 'https://m.avito.ru/profile/login',
    'Host': 'm.avito.ru',
    'Cookie':   'u=2fgxopb9.1dgwiyy.g1qmlglqmd;'
                'v=1557232049;'
                'f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e'
                '06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b'
                '89268a7bf63aa148d27b0d53c7afc06d0b3c02ea8f64acc0bd71e7cb57bbcb8e0f8efbe2d36a658de01ad70e105b68734'
                '8fa4d7ea84258c63d59c9621b2c0fa58fbed76bde8afb15d2fb0fb526bb39450a143114829cf33ca7e2415097439d4047'
                'd99271d186dc1cd046b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd'
                '50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa24a135baa76198de30af1817fda3ee138dfbaf9591eb0125c2'
                '2c73d05cd75827e9148c4b87c1d0ed34cf9c8992779b7543751e8db413f67458e824b76b5480d720e1566815473f745c0'
                'f7387369bacb58732de926882853a915ac1de0d034112915ac1de0d034112915ac1de0d034112e361ecdd2773a3a32ccf'
                '4030d58d09bbf722fe85c94f7d0c2da10fb74cac1eab5583812d2faa33d8;'
                'buyer_selected_search_radius4=0_general;'
                '_ga=GA1.2.2139619629.1554375120;'
                '_gid=GA1.2.1523018365.1557232054;'
                '_ym_uid=1554375121402443899;'
                '_ym_d=1554375121;'
                '_fbp=fb.1.1554375121116.11543209;'
                'cto_lwid=aa5de296-f4b7-4dc2-a82c-9b6301d05698;'
                '_ym_isad=2;'
                '_ym_visorc_24618824=b;'
                'anid=646eb173a2060e4516097a307d934a75%3B0;'
                'sessid=29d138a109485a4876e50d21117d0a2e.1557233839;'
                'dfp_group=92;'
                '_mlocation=647420;'
                'k-cookie=4ad4e0d9c3308f7cfa05c81c44b3e2b1b920bd4b;'
                'abp=0',
    'Content-type': 'application/x-www-form-urlencoded'
}


DEFAULT_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/'
                  'signed-exchange;v=b3',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'u=2fgxopb9.1dgwiyy.g1qmlglqmd;'
                  '_ga=GA1.2.787839117.1550752754;'
                  '_fbp=fb.1.1550752754027.1309230693;'
                  '_ym_uid=1550752754172788459;'
                  '_ym_d=1550752754;'
                  '__gads=ID=aa4f41e1d4691557:T=1550752948:S=ALNI_MbcuKzt-jMpK82KekqS44Rvyw3YgQ;'
                  'buyer_location_id=646710;'
                  '__utmz=99926606.1551856488.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);'
                  'cto_lwid=331c2981-71ff-4c18-91b9-32e42a394852;'
                  'buyer_selected_search_radius4=0_general;'
                  '__utma=99926606.787839117.1550752754.1555507406.1556515479.3;'
                  '_mlocation=647420;'
                  'v=1557232049;'
                  'dfp_group=43;'
                  'f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06c'
                  'b59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df1'
                  '03df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a0df103df0c26013ae2bfa4611aac769efa4d7ea8'
                  '4258c63d74c4a16376f87ccd897baa7410138eadfb0fb526bb39450a46b8ae4e81acb9fae2415097439d4047fb0fb526bb39'
                  '450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264ed'
                  'd50b96489ab264ed46b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da7e87a84e371fc60d21aba'
                  'b15028c5344d5e61d702b2ac73f71b4d31ba3578021fbae804e0bf5c02c086977b8878fcf22eb98f05791aec91c58732de92'
                  '6882853a9d9b2ff8011cc827c4d07ec9665f0b70915ac1de0d0341126e1723f83ba7c15fbb6572da8e9de6fc2da10fb74cac'
                  '1eab2da10fb74cac1eab2d998d7a836f6518517083b9c0063862;'
                  '_gid=GA1.2.1130770504.1558508042;'
                  '_ym_isad=2;'
                  '_ym_visorc_24618824=b;'
                  'rheftjdd=rheftjddVal;'
                  'anid=38052958e2147777232a2c62b6c80508%3B0;'
                  'dfp_group=92;'
                  'weborama-viewed=1;'
                  '_ym_visorc_34241905=w;'
                  'abp=0;'
                  '_dc_gtm_UA-2546784-1=1;'
                  'sessid=29d138a109485a4876e50d21117d0a2e.1557233839;'
                  'criteo_write_test=ChUIBBINbXlHb29nbGVSdGJJZBgBIAE',
        'DNT': '1',
        'Host': 'm.avito.ru',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }


proxies = {'http': 'http://user24145:eshj54@5.188.72.179:6676'}
s = requests.Session()

r = s.get('https://m.avito.ru/', headers=DEFAULT_HEADERS, proxies=proxies)
# print(r.headers['Set-Cookie'])
# print(r.cookies)

data = {'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
        'login': 'deit91@yandex.ru',
        'password': 'M3244dmk'
        }

r = s.post('https://m.avito.ru/api/9/auth?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir', headers=LOGIN_HEADERS,
           proxies=proxies, data=data)
print(r.text)
