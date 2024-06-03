from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'luego doy clik en el boton de lista de cuentas bancarias')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities2"]/div/a[1]').click()


@given(u'luego doy clik en el boton de eliminar cuenta')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="dataTable"]/tbody/tr[3]/td[6]/a[1]').click()


@when(u'presiono el boton de confirmar eliminación de la cuenta bancaria')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/form/button').click()


@then(u'no puedo ver el nombre el id "{id_cuenta}" en la lista de cuentas')
def step_impl(context, id_cuenta):
    cuentas = context.driver.find_elements(
        By.XPATH,
        '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for cuenta in cuentas:
        if cuenta.find_element(By.XPATH, 'td[1]').text == id_cuenta:
            assert False, f"La cuenta con id {id_cuenta} se encuentra en la lista de cuentas"
    time.sleep(3)
    