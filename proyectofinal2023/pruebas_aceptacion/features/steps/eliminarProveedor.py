from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given(u'luego doy clik en el boton de lista proveedores')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseTwo"]/div/a[1]').click()


@given(u'luego doy clik en el boton de eliminar')
def step_impl2(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="dataTable"]/tbody/tr[3]/td[9]/a[1]').click()


@when(u'presiono el boton de confirmar eliminación')
def step_impl3(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/form/button').click()
    time.sleep(3)


@then(
    u'ya no puedo ver al proveedor con rfc "{rfc}" en la lista de proveedores'
)
def step_impl4(context, rfc):
    proveedores = context.driver.find_elements(
        By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for proveedor in proveedores:
        if proveedor.find_element(By.XPATH, 'td[1]').text == rfc:
            assert False, f"El proveedor con rfc {
                rfc} se encuentra en la lista de proveedores"
    time.sleep(3)
