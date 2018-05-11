# coding=utf-8
# user=hu
import re
import os
import time
import cv2 as cv
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        driver.get(sliding_url)
        time.sleep(20)
        break
    # time.sleep(1)

print(driver.title)
driver.quit()
if __name__ == '__main__':
    pass