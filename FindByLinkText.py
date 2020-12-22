#!/usr/bin/env python3
# 

from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbylinkedtext = driver.find_element_by_link_text('Login')

        if elementbylinkedtext is not None:
            print("Found element by Link Text")

        elementbypartiallinkedtext = driver.find_element_by_partial_link_text('Pract')

        if elementbypartiallinkedtext is not None:
            print('We found an element by Partial Link Text')


ff = FindByLinkText()
ff.test()