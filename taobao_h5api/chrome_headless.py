# coding=utf-8
# user=hu
import re
import os
import time
import cv2 as cv
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import win32gui
# import win32api
# from win32gui import *
import pyautogui


def my_pyautogui():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth/2, screenHeight/2)



titles = set()


def foo(hwnd, mouse):
    # 去掉下面这句就所有都输出了，但是我不需要那么多
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        titles.add(GetWindowText(hwnd))


# EnumWindows(foo, 0)
# lt = [t for t in titles if t]
# lt.sort()
# for t in lt:
#     print(t)


def windows_api():
    classname = 'notepad'
    # titlename = '无标题-记事本'
    t = '无标题 - 记事本'
    hwnd = win32gui.FindWindow(classname, t)
    l, t, r, b = win32gui.GetWindowRect(hwnd)


def firs():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
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
    for i in range(50):
        driver.refresh()
        if len(driver.page_source) < 10000:
            html = driver.page_source
            # print(driver.page_source)
            sliding_url = re.findall(u'https://.*?com/', html, re.I)[0]
            print(sliding_url)
            # driver.get(sliding_url)
            time.sleep(50)
            break
        # time.sleep(1)

    print(driver.title)
    driver.quit()


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
    # windows_api()
    pass