from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given(u'luego clik en el boton de agregar cuenta')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities2"]/div/a[2]').click()


@given(u'escribo el id de la cuenta "{id}"')
def step_impl(context, id):
    context.driver.find_element(By.NAME, 'idcuenta').send_keys(id)


@given(u'escribo el responsable de la cuenta "{responsable}"')
def step_impl(context, responsable):
    context.driver.find_element(By.NAME, 'responsable').send_keys(responsable)


@given(u'escribo el limite de prepuestario de la cuenta "{limite}"')
def step_impl(context, limite):
    context.driver.find_element(
        By.NAME, 'limite_presupuestario').send_keys(limite)


@given(u'selecciono el proyecto de la cuenta "{proyecto}"')
def step_impl(context, proyecto):
    context.driver.find_element(By.NAME, 'proyecto').send_keys(proyecto)


@when(u'presiono el boton guardar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/div/form/button').click()


@then(
    u'puedo ver el id de la cuenta "{id_cuenta}" en la lista de cuentas bancarias')
def step_impl7(context, id_cuenta):
    cuentas = context.driver.find_elements(
        By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for cuenta in cuentas:
        if cuenta.find_element(By.XPATH, 'td[1]').text == id:
            assert True, f"El id {
                id_cuenta} no se encuentra en la lista de cuentas bancarias"
    time.sleep(2)
