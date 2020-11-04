#!/usr/bin/env python3
# Selenium Tutorial #1
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
driver.get("https://techwithtim.net")
print(driver.title)

# ex: 1 find the search field and search for "test"
search = driver.find_element_by_name("s")
time.sleep(10)
search.send_keys("test")
search.send_keys(Keys.RETURN)
# keep the browser open for a bit
time.sleep(20)


# ex: 2 find specific articles from string search
main = driver.find_element_by_id("main")
print(main.text)

# ex: 3 
#try:
    # wait up to 10 seconds for the element
 #   main = WebDriverWait(driver, 10).until(
 #       EC.presence_of_element_located((By.ID, "main"))
 #   )
    ## ex: 3.1 prints all to STDOUT
    ## print(main.text)

    # ex: 3.2 print the searched article headers to STDOUT
    #articles = main.find_elements_by_tag_name("article")
    #for article in articles:
    #    header = article.find_element_by_class_name("entry-summary")
    #    print(header.text)

#finally:
#    driver.close()




# close the test window
driver.close()