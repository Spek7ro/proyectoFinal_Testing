from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@given(u'le doy clik en el enlace Cuentas Bancarias')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Cuentas Bancarias').click()


@given(u'luego clik en el boton de lista de cuentas bancarias')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities2"]/div/a[1]').click()
    time.sleep(1)
