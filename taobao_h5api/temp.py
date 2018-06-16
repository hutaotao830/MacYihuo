# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from socket import *
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
import win32com.client as c


def my_socket():
    print('waiting')
    udpscoket = socket(AF_INET, SOCK_DGRAM)
    bindaddr = ('', 12345)
    udpscoket.bind(bindaddr)
    i = 1
    while i < 1000000:
        i += 1
        recvData = udpscoket.recvfrom(10240)
        url = recvData[0].decode('ascii')
        print(len(url))
        my_http(url)
    udpscoket.close()
    

def my_http(url):
    chrome_option = Options()
    #chrome_options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36')
    mobile_emulation = {"deviceName":"iPhone X"}
    chrome_option.add_experimental_option("mobileEmulation", mobile_emulation)
    
    driver = webdriver.Chrome(
            #chrome_options=chrome_option
            )
    driver.get(url)
    time.sleep(3)
    
    shell = c.Dispatch('WScript.Shell')
    shell.SendKeys('{F12}', 0)
    time.sleep(4)
    shell.SendKeys('^+m', 0)
    
    time.sleep(5)

    print('Go to find element.')
    if 1:
        try:
            element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[@id="nc_1_n1z"]'))
                    )
        except Exception as e:
            print('Not find element!', e)
            driver.quit()
            return 1
    #print('After if.')
    #element = driver.find_element_by_class_name('button')
    #element = driver.find_element_by_id('nc_1_n1z')
    print('Element is: ', element)
    action = TouchActions(driver)
    action.flick_element(element, 160, 0, 190).perform()
    #action.scroll_from_element(element=element, ).perform()
    #dr1 = ActionChains(driver)
    #dr1.click_and_hold(element).pause(1)
    #dr1.move_by_offset(100, 0).pause(1).move_by_offset(160, 0)
    #dr1.perform()
    time.sleep(1)
    print(driver.title)
    time.sleep(10)
    driver.quit()

def my_http2(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    shell = c.Dispatch('WScript.Shell')
    shell.SendKeys('{F12}', 0)
    time.sleep(4)
    shell.SendKeys('^+m', 0)
    time.sleep(2)
    dr1 = ActionChains(driver)
    driver.find_element_by_id('sb_form_q').send_keys('hu')
    driver.find_element_by_id('sb_form_q').send_keys(Keys.F12)
    driver.find_element_by_id('sb_form_q').send_keys('yang')
    
    print('Send huyangjie')
    time.sleep(3)
    dr1.send_keys(Keys.SHIFT+Keys.CONTROL+'i')
    dr1.key_down(Keys.F12).pause(0.1).key_up(Keys.F12).perform()
    print('Send F12')
    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    print('run')
    # my_socket()
    url = 'http://www.bing.com'
    my_socket()
    pass