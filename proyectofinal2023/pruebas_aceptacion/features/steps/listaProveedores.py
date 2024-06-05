from behave import given, then
from selenium.webdriver.common.by import By
import time


@given(u'luego clik en el boton de Lista')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="collapseTwo"]/div/a[1]').click()


@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    div = context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[1]/h4')
    time.sleep(3)
    assert div.text, f"El {mensaje} no se encuentra en {div.text}"
    time.sleep(1)
