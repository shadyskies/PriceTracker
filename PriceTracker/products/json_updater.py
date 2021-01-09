#!/usr/bin/env python3 

import json

import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def flipkart():
    url = input()
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    div_tag = soup.find_all('div', {"class": "_30jeq3 _16Jk6d"})
    price = div_tag[0].get_text()
    return price.strip('₹')


# def amazon_scrape():
#     url = input()
#     page = requests.get(url, headers=HEADERS)
#     soup = BeautifulSoup(page.content, features='html.parser')
#     span_tag = soup.find_all('span', {"class": "a-price-whole"})
#     print(span_tag)
#     price = span_tag[0].get_text()
#     return price


def paytm():
    url = input()
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('div', {"class": "_1kMS"})
    # print(span_tag)
    price = span_tag[0].get_text()
    return price


def snapdeal():
    query = 'mobile phone'
    url = 'https://www.snapdeal.com/search?keyword=' + query
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('span', {"class": "product-price"})
    return (span_tag[0].get_text())


def amazon():
    query = 'bodywash'
    url = 'https://www.amazon.in/s?k=' + query
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('span', {"class": "a-price-whole"})
    return span_tag

def json_update(json_file, curr_dtime, price_dict):
    # print(json_file)
    # print(curr_dtime)
    # for appending prices
    # print(json_file)
    for i in price_dict.keys():
        tmp = json_file['websites'][i]
        tmp.append(price_dict[i])
        json_file['websites'][i] = tmp
    # for appending datetime
    tmp = json_file['datetime']
    tmp.append(str(curr_dtime))
    json_file['datetime'] = tmp
    # print(json_file)
    with open('temp.json', 'w') as j_out:
        json.dump(json_file, j_out)


if __name__ == '__main__':
    # with open('temp.json','r') as file:
    #     json_update(json.load(file), datetime.datetime.now(), {'amazon': 20202,'flipkart': 20212})
    # print(flipkart_scrape())
    # print(amazon_scrape())
