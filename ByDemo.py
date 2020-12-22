#!/usr/bin/env python3
# 

from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():
    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbyid = driver.find_element(By.ID, 'name')

        if elementbyid is not None:
            print("Found element by Id")

        elementbyxpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementbyxpath is not None:
            print('Found element by Xpath')

        elementbylinktext = driver.find_element(By.LINK_TEXT, 'Login')
        
        if elementbylinktext is not None:
            print('Found element by link text')


ff = ByDemo()
ff.test()

class ListOfElements():

    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementlistbyclassname = driver.find_elements_by_class_name('inputs')
        length = len(elementlistbyclassname)

        if elementlistbyclassname is not None:
            print(f'ClassName -> Size of the list is: {length} ')

            elementlistbytagname = driver.find_elements(By.TAG_NAME, 'td')
            length2 = len(elementlistbytagname)

        if elementlistbytagname is not None:
            print(f'TagName -> Size of the list is: {length2} ')

ff = ListOfElements()
ff.test()

