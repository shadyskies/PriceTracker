#!/usr/bin/env python3 

import os
import json
import datetime
import requests
from bs4 import BeautifulSoup


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def flipkart_scrape():
    url = input()
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    div_tag = soup.find_all('div', {"class": "_30jeq3 _16Jk6d"})
    price = div_tag[0].get_text()
    # print(soup)
    # prod_class = soup.select_one("a-size-medium a-color-price priceBlockBuyingPriceString")
    # prod = prod_class.select_one("span")
    # title =
    # try:
    #     price = float(soup.find(id='priceblock_ourprice').get_text())
    # except Exception:
    #     price = ''
    #     print("No product found")
    return price.strip('₹')

# def amazon_scrape():
#     url = input()
#     page = requests.get(url, headers=HEADERS)


def json_update(json_file,curr_dtime, price_dict):
    # print(json_file)
    # print(curr_dtime)
    #for appending prices
    # print(json_file)
    for i in price_dict.keys():
        tmp = json_file['websites'][i]
        tmp.append(price_dict[i])
        json_file['websites'][i] = tmp
    #for appending datetime
    tmp = json_file['datetime']
    tmp.append(str(curr_dtime))
    json_file['datetime'] = tmp
    # print(json_file)
    with open('temp.json', 'w') as j_out:
        json.dump(json_file, j_out)


if __name__ == '__main__':
    with open('temp.json','r') as file:
        json_update(json.load(file), datetime.datetime.now(), {'amazon': 20202,'flipkart': 20212})
    # print(flipkart_scrape())
