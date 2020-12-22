#!/usr/bin/env python3
# Behave Intro
# 

from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('open Costco homepage')
def openHomePage(context):
    context.driver.get('https://costco.com')

@then('verify the cart is present on the Page')
def VerifyLogo(context):
    status = context.driver.find_element_by_id('cart-d').is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()


