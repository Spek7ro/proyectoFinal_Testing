from behave import given
from selenium.webdriver.common.by import By
import time


@given(u'le doy clik en el enlace costos')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Costos').click()


@given(u'luego clik en el boton de lista de costos')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="collapseUtilities3"]/div/a[1]').click()
    time.sleep(3)
