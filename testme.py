#!/usr/bin/src python3
# Selenium Tutorial #1
# 
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://nytimes.com")
headlines = driver.find_elements_by_class_name("story-heading")