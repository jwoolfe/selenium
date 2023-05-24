#!/usr/bin/env python3
# 

from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)
        elementbyxpath = driver.find_element_by_xpath('//input[@id="name"]')

        if elementbyxpath is not None:
            print("Found element by XPATH")

        elementbycss = driver.find_element_by_css_selector('div.block:nth-child(4)')

        if elementbycss is not None:
            print('We found an element by CSS')


ff = FindByXpathCss()
ff.test()