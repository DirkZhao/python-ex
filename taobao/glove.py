#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 上午11:08
# @Author  : Dirk Zhao
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq

#不加载图片，节省时间
SERVICE_ARGS=['--load-images=false']
# driver = webdriver.PhantomJS(service_args=SERVICE_ARGS, executable_path="/Users/dirkzhao/Code/python-ex/drivers/phantomjs")
driver = webdriver.Firefox(executable_path='/Users/dirkzhao/Code/python-ex/drivers/geckodriver')
index_url = 'https://www.taobao.com/'
wait = WebDriverWait(driver, 10)
KEYWORD = '手套'
FileName = '/Users/dirkzhao/Code/python-ex/data/'+KEYWORD+'.csv'


def search(keyword):
    try:
        driver.get(index_url)
        user_search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        user_search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search")))
        user_search_input.send_keys(keyword)
        user_search_button.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.total')))
        total_page = re.compile(r'(\d+)').search(total.text).group(1)
        print(total_page)
        return int(total_page)
    except TimeoutError:
        search(keyword)


def get_next_page(pageNum):
    try:
        user_page_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/div[2]/input")))
        user_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/div[2]/span[3]")))
        user_page_input.clear()
        user_page_input.send_keys(pageNum)
        user_page_button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.active > span:nth-child(1)'), str(pageNum)))
        get_products()
    except TimeoutError:
        get_next_page(pageNum)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.grid > div:nth-child(1)')))
    html = driver.page_source
    doc = pq(html)
    items = doc('div.item').items()
    for item in items:
        product = {
            'url': item('a.pic-link').attr('href'),
            'price': item.find('.price').text()[1:],
            'amount': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_csv(product)


def save_to_csv(product):
    with open(FileName, 'a', encoding='gb18030') as f:
        s = product['title'] + ',' + product['price'] + ',' + product['amount'] + ',' + product['location'] + ',' + \
            product['shop'] + ',' + product['url'] + '\n'
        try:
            f.write(s)
            print('保存到csv成功', product)
        except:
            pass


def main():
    total = search(KEYWORD)
    for i in range(2, total+1):
        get_next_page(i)
    driver.close()


if __name__ == '__main__':
    main()
