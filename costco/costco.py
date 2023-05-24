#!/usr/bin/env python3
# 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# set up the path to the chromedriver
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

# open the page and print the title to STDOUT
driver.get("https://costco.com")
print(driver.title)

# ex: 1 find the search field and search for "test"
search = driver.find_element_by_id("search-field")
search.send_keys("tree")
search.send_keys(Keys.RETURN)
# keep the browser open for a bit
time.sleep(10)


# ex: 2 find specific articles from string search
main = driver.find_element_by_id("header_sign_in")
print(main.header)



# close the test window
driver.close()