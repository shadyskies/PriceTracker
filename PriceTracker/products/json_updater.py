#!/usr/bin/env python3 

import os
import json

import requests
from bs4 import BeautifulSoup
import datetime

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def flipkart(url):
    # url = input()
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


def paytm(url):
    # url = input()
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('div', {"class": "_1kMS"})
    # print(span_tag)
    price = span_tag[0].get_text()
    return price


def snapdeal(query):
    # query = 'mobile phone'
    url = 'https://www.snapdeal.com/search?keyword=' + query
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('span', {"class": "product-price"})
    return (span_tag[0].get_text())


def amazon(query):
    # query = 'bodywash'
    url = 'https://www.amazon.in/s?k=' + query
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, features='html.parser')
    span_tag = soup.find_all('span', {"class": "a-price-whole"})
    # print(span_tag)
    price = span_tag[0].get_text()
    return price


def json_update(url, username):
    website = ""
    price = 0
    if "www" not in url:
        price = amazon(url)  # actually query and not url
        website = "amazon"
        # sna_pr = snapdeal(url) #same
    elif "flipkart" in url:
        price = flipkart(url)
        website = "flipkart"
    elif "paytm" in url:
        price = paytm(url)
        website = "paytm"
    filepath = str("../json_files/") + username + str(".json")

    with open(filepath, "r") as json_file:
        json_file = json.load(json_file)
        tmp = json_file["website"][website]
        tmp.append(price)
        json_file["website"][website] = tmp
        tmp = json_file["datetime"]
        curr_dtime = datetime.datetime.now()
        tmp.append(str(curr_dtime))
        json_file['datetime'] = tmp
        with open(filepath, "w") as j_out:
            json.dump(json_file, j_out)


def main_price_getter_initial_json_create(username, url):
    # print("shitty code")
    if "www" not in url:
        price = amazon(url)  # actually query and not url
        website = "amazon"
        # sna_pr = snapdeal(url) #same
    elif "flipkart" in url:
        price = flipkart(url)
        website = "flipkart"
    elif "paytm" in url:
        price = paytm(url)
        website = "paytm"
    filepath = str("../json_files/") + username + str(".json")
    with open(filepath, "w") as file:
        curr_dtime = str(datetime.datetime.now())
        json_dict = {"username": username, "website": {website: [price]}, "datetime": [curr_dtime]}
        json.dump(json_dict, file)


def check_json_exists(username):
    filepath = str("../json_files/") + username + ".json"
    if os.path.exists(filepath):
        return 1
    else:
        return 0
