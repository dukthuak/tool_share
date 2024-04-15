import sys
import os
import requests
import threading
import time
__AUTHOR__ = 'B07VNB07VN'
__CONTACT__ = 'https://www.facebook.com/profile.phamthanhbinh'
def banner():
    print(f''' 
       \033[1;32mAuthor: \x1b[38;2;233;233;233m{__AUTHOR__}\033[0m           
       \033[1;32mContact: \x1b[38;2;233;233;233m{__CONTACT__} \033[0m                                                                                               ''')
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
gome_token = []
def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',

        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
    
def main_share():
    clear()
    banner()
    input_file = open(input("\033[1;31mFILE COOKIE : \x1b[38;2;233;233;233m")).read().split('\n')
    id_share = input("\033[1;31mID POST : \x1b[38;2;233;233;233m")
    total_share = int(input("\033[1;31mJOB : \x1b[38;2;233;233;233m"))
    delay = int(input("\033[1;31mTIME DELAY : \x1b[38;2;233;233;233m"))
    print('\x1b[38;2;0;255;255m════════════════════════════════════\x1b[38;2;233;233;233m')
    print('\033[1;31m[*] \x1b[38;2;233;233;233mwaiting...', end='\r')
    all = get_token(input_file)
    total_live = len(all)
    print(f'\033[1;31mLive: \x1b[38;2;233;233;233m{total_live} \033[1;31mCookies')
    if total_live == 0:
        sys.exit()
    print('\x1b[38;2;0;255;255m════════════════════════════════════\x1b[38;2;233;233;233m')
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'\033[1;31mShare: + \x1b[38;2;233;233;233m{stt}', end='\r')
            time.sleep(delay)
        if stt > total_share:
            break
    gome_token.clear()
    input('\033[1;31m[*] \x1b[38;2;0;255;255mDONE| ENTER...\033[0m')
while True:
    try:
        main_share()
    except KeyboardInterrupt:
        print('\033[1;31m[*] \x1b[38;2;0;255;255mTHANK YOU...\033[0m')
        sys.exit()