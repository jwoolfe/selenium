#!/usr/bin/env python3
# Selenium Tutorial #1
# 

# Test ChromeDriver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")

# Test GeckoDriver
driver = webdriver.Firefox()
driver.get('https://www.seattletimes.com')
headlines = driver.find_elements_by_class_name('story-heading')
