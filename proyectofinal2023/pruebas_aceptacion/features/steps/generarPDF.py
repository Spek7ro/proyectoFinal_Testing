from behave import given, when, then
from selenium.webdriver.common.by import By
import time
import os


@given(u'luego doy clik en el boton de lista de proveedores')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseTwo"]/div/a[1]').click()


@given(u'luego doy clik en el boton de lista de proyectos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities"]/div/a[1]').click()


@given(u'luego doy clik en el boton de generar reporte pdf')
def step_impl(context):
    context.driver.find_element(
        By.XPATH,
        '//*[@id="content"]/div/div/div/div[2]/div/form/a[2]').click()
    time.sleep(2)


@given(u'guardo el archivo pdf en "{ruta}" con el nombre "{nombre}"')
def step_impl(context, ruta, nombre):
    download_dir = ruta
    pdf_filename = nombre
    os.path.join(download_dir, pdf_filename)


@then(u'ingreso a la url "{ruta}" y puedo ver el pdf')
def step_impl(context, ruta):
    assert os.path.exists(ruta), f"El archivo PDF no se encuentra en {ruta}"
    # Abrir el archivo pdf en el navegador
    context.driver.get(f'file://{ruta}')
    time.sleep(2)
