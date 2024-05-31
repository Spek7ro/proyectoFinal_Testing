from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'le doy clik en el enlace proyectos')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Proyectos').click()
    time.sleep(1)
    
@given(u'luego clik en el boton de lista de proyectos')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="collapseUtilities"]/div/a[1]').click()    
    