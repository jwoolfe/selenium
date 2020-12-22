#!/usr/bin/env python3
# 

from selenium import webdriver

class FindByClassTag():
    def test(self):
        baseurl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseurl)

        elementbyclassname = driver.find_element_by_class_name('displayed-class')
        elementbyclassname.send_keys('Testing the Element')

        if elementbyclassname is not None:
            print('Found element by Class Name')

        elementbytagname = driver.find_elements_by_tag_name('h1')
        text = elementbytagname.element

        if elementbytagname is not None:
            print(f'Found element by tag name {text}')


ff = FindByClassTag()
ff.test()