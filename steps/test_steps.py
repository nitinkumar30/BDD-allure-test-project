import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from config.configreader import *

from utils import *


@given('User is on login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(get_property_value('URL'))
    addScreenshot(context, '1')
    time.sleep(2)


@when('User provides valid login credentials')
def step_impl(context):
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHusername')).send_keys(
        get_property_value('username'))
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHpassword')).send_keys(
        get_property_value('password'))
    addScreenshot(context, '2')
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHloginBtn')).click()


@when('User provides valid login credentials as {username} and {password}')
def step_impl(context, username, password):
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHusername')).send_keys(username)
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHpassword')).send_keys(password)
    addScreenshot(context, '2')
    context.driver.find_element(By.XPATH, get_loginPage_xpath_value('XPATHloginBtn')).click()


@then('User will be logged into website')
def step_impl(context):
    time.sleep(2)
    assert context.driver.title == get_property_value(
        'titleHomepage'), 'Wrong title captured or wrong web portal redirected !'
    addScreenshot(context, '3')
    context.driver.quit()


@then('User will be displayed with a current page title')
def step_impl(context):
    time.sleep(2)
    assert context.driver.title == get_property_value(
        'titleHomepage'), 'Wrong title captured or wrong web portal redirected !'
    addScreenshot(context, '3')
    context.driver.quit()
