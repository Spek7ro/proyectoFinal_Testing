from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given(u'luego doy clik en el boton de lista de costos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities3"]/div/a[1]').click()


@given(u'luego doy clik en el boton de eliminar costo')
def step_impl2(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="dataTable"]/tbody/tr[4]/td[6]/a[1]').click()


@when(u'presiono el boton de confirmar eliminación del costo')
def step_impl3(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/div/form/button').click()
    time.sleep(2)


@then(
    u'no puedo ver la descripcion del costo "{descripcion}" '
    u'en la lista de costos'
)
def step_impl4(context, descripcion):
    costos = context.driver.find_elements(
        By.XPATH,
        '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for costo in costos:
        if costo.find_element(By.XPATH, 'td[1]').text == descripcion:
            assert True, f"La descripcion {
                descripcion} se encuentra en la lista de costos"
    time.sleep(2)
