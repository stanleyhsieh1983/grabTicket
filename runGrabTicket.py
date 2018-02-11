#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 09:38:44 2018

@author: stanley
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

chromeDriver = 'xxxxxx/chromedriver' #webrowser driver

sourceURL = 'https://tixcraft.com/'
targetURL = 'https://tixcraft.com/activity/detail/18_JACKY'

googleID = 'xxxxxx'
googlePW = 'xxxxxx'

# open webbrowser
browser = webdriver.Chrome(chromeDriver)
browser.maximize_window()

# open webpage
browser.get(sourceURL)

# login
browser.find_element_by_xpath('//*[@id="header"]/div[2]/div[3]/span/div/div[1]/a').click()
sleep(1)

browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div/div[2]/a/img').click()
sleep(1)

inputElement0 = browser.find_element_by_xpath('//*[@id="identifierId"]')
inputElement0.send_keys(googleID)
browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
sleep(1)

inputElement1 = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
inputElement1.send_keys(googlePW)
browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
sleep(1)

# open webpage
browser.get(targetURL)

# click order ticket
while  True:
    try:
        print "[order]"
        browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/ul/li[1]/a/div/span').click()
        break
    except:
        continue

# click buy ticket
while  True:
    try:
        print "[date]"
        browser.find_element_by_name('yt4').click()
        break
    except:
        continue

## select seat
#browser.find_element_by_id('3011_1').click()
#
## agreement
#browser.find_element_by_name('TicketForm[agree]').click()
#
## quantity
#select = Select(browser.find_element_by_name('TicketForm[ticketPrice][01]'))
#select.select_by_value('1')
#
#print 'please input verification code manually !'

