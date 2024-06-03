from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given(u'luego doy clik en el boton de lista proyectos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities"]/div/a[1]').click()

@given(u'luego doy clik en el boton de eliminar proyecto')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="dataTable"]/tbody/tr[6]/td[9]/a[1]').click()

@when(u'presiono el boton de confirmar eliminación del proyecto')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/form/button').click()

@then(u'no puedo ver el nombre del proyecto "{nombre}" en la lista de proyectos')
def step_impl(context, nombre):
    proyectos = context.driver.find_elements(
        By.XPATH,
        '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for proyecto in proyectos:
        if proyecto.find_element(By.XPATH, 'td[1]').text == nombre:
            assert False, f"El proyecto {nombre} se encuentra en la lista de proyectos"
    time.sleep(3)
    