#!/usr/bin/env python3
# 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserInteractions():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()

        # Window Maximize
        driver.maximize_window()

        # Open the URL
        driver.get(baseurl)

        # Get Title
        print(f"Title of the web page is: {driver.title}")
    
        # Get Current URL
        print(f"Current URL of the web page is: {driver.current_url}")

        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Open another URL
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        print(f'Current url of webpage is: {driver.current_url}')

        # Browser Back
        driver.back()
        print("Go one step back in browser history")
        print(f'Current url of webpage is: {driver.current_url}')

        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        print(f'Current url of webpage is: {driver.current_url}')

        # Get Page Source
        #print(driver.page_source)

        # Browser Close / Quit
        driver.close()
        driver.quit()


class ClickAndSendKeys():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        loginlink = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div/ul/li[2]/a")
        loginlink.click()

        emailfield = driver.find_element(By.ID, "user_email")
        emailfield.send_keys("test")

        passwordfield = driver.find_element(By.ID, "user_password")
        passwordfield.send_keys("test")

        time.sleep(5)

        emailfield.clear()

        time.sleep(5)

        passwordfield.send_keys("test")

class ElementState():

    def isEnabled(self):
        baseurl = "http://www.google.com"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_name("q")
        e1state = e1.is_enabled()   # True for enabled, False for disabled
        print(f"E1 is Enabled? -> {str(e1state)} ")
        e1.send_keys("letskodeit")

class RadioButtonsAndCheckboxes():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        bmwradiobutton = driver.find_element_by_id("bmwradio")
        bmwradiobutton.click()

        time.sleep(2)
        benzradiobutton = driver.find_element_by_id("benzradio")
        benzradiobutton.click()

        time.sleep(2)
        bmwcheckbox = driver.find_element_by_id("bmwcheck")
        bmwcheckbox.click()

        time.sleep(2)
        benzcheckbox = driver.find_element_by_id("benzcheck")
        benzcheckbox.click()

        print(f"BMW Radio Button is selected? {str(bmwradiobutton.is_selected())}")
        print(f"Benz Radio Button is selected? {str(benzradiobutton.is_selected())}")
        print(f"BMW Check Box is selected? {str(bmwcheckbox.is_selected())}")
        print(f"Benz Check Box is selected? {str(benzcheckbox.is_selected())}")


## Go
#ff = ElementState()
#ff.isEnabled()
#
#ff = BrowserInteractions()
#ff = test()
#
##ff = ClickAndSendKeys()
##ff.test()

ff = RadioButtonsAndCheckboxes()
ff.test()