#!/usr/bin/env python3
# 

from selenium import webdriver

class FindByIdName():
    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)
        elementbyid = driver.find_element_by_id('name')

        if elementbyid is not None:
            print("Found element by Id")

        elementbyname = driver.find_element_by_name('show-hide')

        if elementbyname is not None:
            print('We found an element by Name')


ff = FindByIdName()
ff.test()