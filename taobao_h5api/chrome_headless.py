# coding=utf-8
# user=hu
import re
import os
import time
import cv2 as cv
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import win32clipboard as w
import win32con
import json
import mysql.connector

# conn = mysql.connector.connect(user='root', password='mysql', database='mysql', host='192.168.31.3')
# sql_str = 'insert into log_table(result,dates,nexttime) values(%s,%s,%d)'


def first():
    cookies_url = 'https://api.xiaoyataoke.com/api/XiaoYaTaoKe/AddV6Cookie?shop_name=ZzZrdWd1Vk8zWXFISHM2TVNlMlFKRlNLL3ZjWXlaTTU=&data_source=huyangjie&cookies=x5sec='

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 '
                                '(KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(640, 1136)
    url = "https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.4.8&appKey=12574478&t=1514363050271" \
          "&sign=58c772297bca044c441667acae13e869&api=mtop.taobao.detail.getdetail&v=6.0&ttid=2016%40taobao_h5_2.0.0" \
          "&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1" \
          "&data=%7B%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22543736245887%5C%22%2C%5C%22abtest%5C%22%3A%5C%222" \
          "%5C%22%2C%5C%22rn%5C%22%3A%5C%2214f65a30b76082ef68a59833849b2b8f%5C%22%2C%5C%22sid%5C%22%3A%5C%2242b9f87ba" \
          "47a92e8b98e1621576c32dd%5C%22%7D%22%2C%22itemNumId%22%3A%22543736245887%22%7D&qq-pf-to=pcqq.c2c"
    driver.get(url)
    for i in range(550):
        driver.refresh()
        if '挤爆' in driver.page_source:
            print('sliding_url is get.')
            html = driver.page_source
            # print(driver.page_source)
            time.sleep(15)
            sliding_url = re.findall(u'https://.*?com/', html, re.I)[0]
            # print(sliding_url)
            # driver.get(sliding_url)
            time.sleep(1)
            cookies = auto_run(sliding_url)
            if 130 < len(cookies) <= 144:
                print('Sending cookies!')
                send_cookies_url = cookies_url+cookies+';'
                # print(send_cookies_url)
                driver.get(send_cookies_url)
            time.sleep(55)
            break
        # time.sleep(1)

    # print(driver.title)
    driver.quit()


def getText():
    print('get copy.')
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d


def auto_run(url):
    print('auto run.')
    ad_x, ad_y = 95, 34
    # 魅族手机x5sec位置
    x5_x, x5_y = 995, 148
    # 三星手机x5sec位置
    # x5_x, x5_y = 995, 231
    sl_x, sl_y = 154, 918
    pyautogui.moveTo(sl_x, sl_y)
    pyautogui.doubleClick()
    # pyautogui.hotkey('alt', 'backspace', 'X')
    # 最大化窗口
    # pyautogui.hotkey('altleft', 'space', 'X')
    pyautogui.keyDown('altleft')
    time.sleep(0.1)
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyDown('x')
    time.sleep(0.1)
    pyautogui.keyUp('x')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    time.sleep(0.1)
    pyautogui.keyUp('altleft')

    time.sleep(1)
    pyautogui.moveTo(ad_x, ad_y)
    pyautogui.doubleClick()
    time.sleep(0.1)
    pyautogui.doubleClick(ad_x, ad_y)
    pyautogui.hotkey('del')
    time.sleep(1.2)
    pyautogui.typewrite(url)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(30)
    pyautogui.moveTo(sl_x, sl_y)
    pyautogui.dragTo(sl_x+400, sl_y, 1)
    time.sleep(2)
    pyautogui.moveTo(x5_x, x5_y)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(3)
    cookies = getText().decode()

    print(cookies, '\n', time.ctime())

    with open('C:\\Users\\Administrator\\Desktop\\web\\x5sec_log.txt', 'a+') as f:
        f.write(str(time.ctime())[4:19]+': ' + str(len(cookies)) + '\n')
    return cookies

    # pyautogui.typewrite('www.baidu.com')
    # pyautogui.press('enter')
    # sliding_x, sliding_y = pyautogui.locateCenterOnScreen('./img/sliding_block.png')
    # address_x, address_y = pyautogui.locateCenterOnScreen('./img/address.png')
    # x5sec_x, x5sec_y = pyautogui.locateCenterOnScreen('./img/x5sec.png')
    # print(sliding_x, sliding_y)
    # print(address_x, address_y)
    # print(x5sec_x, x5sec_y)
    # pyautogui.moveTo(sliding_x, sliding_y)
    # pyautogui.dragTo(sliding_x+500, sliding_y, 1, button='left')


def chrome_webview():
    url = 'chrome://inspect'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    driver.find_element_by_link_text('inspect').chichk()
    time.sleep(20)
    driver.quit()


def imitation_mobile():
    WIDTH = 320
    HEIGHT = 640
    PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
    url = "https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.4.8&appKey=12574478&t=1514363050271" \
          "&sign=58c772297bca044c441667acae13e869&api=mtop.taobao.detail.getdetail&v=6.0&ttid=2016%40taobao_h5_2.0.0" \
          "&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1" \
          "&data=%7B%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22543736245887%5C%22%2C%5C%22abtest%5C%22%3A%5C%222" \
          "%5C%22%2C%5C%22rn%5C%22%3A%5C%2214f65a30b76082ef68a59833849b2b8f%5C%22%2C%5C%22sid%5C%22%3A%5C%2242b9f87ba" \
          "47a92e8b98e1621576c32dd%5C%22%7D%22%2C%22itemNumId%22%3A%22543736245887%22%7D&qq-pf-to=pcqq.c2c"
    for i in range(10):
        driver.get(url)
        if len(driver.page_source) < 10000:
            html = driver.page_source
            # print(driver.page_source)
            sliding_url = re.findall(u'https://.*?com/', html, re.I)[0]
            print(sliding_url)
            # driver.get(sliding_url)
            time.sleep(50)
            break
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    # imitation_mobile()
    print('runing')
    for i in range(10000):
        for h in range(20):
            time.sleep(36.5)
            # print('*_* ')
            with open('C:\\Users\\Administrator\\Desktop\\web\\x5sec_log.txt', 'a+') as f:
                f.write('>')
        with open('C:\\Users\\Administrator\\Desktop\\web\\x5sec_log.txt', 'a+') as f:
            f.write('\n')
        print('*')
        try:
            first()
        except Exception as e:
            print('wrong', e)
    # auto_run()