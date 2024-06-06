from behave import given, then
from selenium.webdriver.common.by import By
import time


@given(u'luego clik en el boton de agregar costo')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities3"]/div/a[2]').click()


@given(u'escribo el la descripcion del costo "{descripcion}"')
def step_impl(context, descripcion):
    context.driver.find_element(By.NAME, 'descripcion').send_keys(descripcion)


@given(u'escribo el costo del costo "{costo}"')
def step_impl(context, costo):
    context.driver.find_element(By.NAME, 'costo').send_keys(costo)


@given(u'selecciono el proyecto del costo "{proyecto}"')
def step_impl(context, proyecto):
    context.driver.find_element(By.NAME, 'proyecto').send_keys(proyecto)


@then(
    u'puedo ver la descripcion del costo "{descripcion}" en la lista de costos')
def step_impl5(context, descripcion):
    costos = context.driver.find_elements(
        By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for costo in costos:
        if costo.find_element(By.XPATH, 'td[1]').text == descripcion:
            assert True, f"El descripcion {
                descripcion} no se encuentra en la lista de costos"
    time.sleep(2)
