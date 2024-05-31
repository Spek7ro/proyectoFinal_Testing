from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given(u'luego clik en el boton de agregar proyecto')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="collapseUtilities"]/div/a[2]').click()

@given(u'escribo el numero del proyecto "{numero_proyecto}"')
def step_impl(context, numero_proyecto):
    context.driver.find_element(By.NAME, 'num_proyecto').send_keys(numero_proyecto)    

@given(u'escribo el nombre del proyecto "{nombre_proyecto}"')
def step_impl(context, nombre_proyecto):
    context.driver.find_element(By.NAME, 'nombre_proyecto').send_keys(nombre_proyecto)

@given(u'escribo el objetivo del proyecto "{objetivo_proyecto}"')
def step_impl(context, objetivo_proyecto):
    context.driver.find_element(By.NAME, 'objetivo').send_keys(objetivo_proyecto)

@given(u'escribo el presupuesto del proyecto "{presupuesto}"')
def step_impl(context, presupuesto):
    context.driver.find_element(By.NAME, 'presupuesto').send_keys(presupuesto)

@given(u'escribo la duracion del proyecto "{duracion}"')
def step_impl(context, duracion):
    context.driver.find_element(By.NAME, 'duracion').send_keys(duracion)

@given(u'escribo el responsable del proyecto "{responsable}"')
def step_impl(context, responsable):
    context.driver.find_element(By.NAME, 'responsables').send_keys(responsable)

@given(u'selecciono al proveedor del proyecto "{proveedor}"')
def step_impl(context, proveedor):
    context.driver.find_element(By.NAME, 'proveedor').send_keys(proveedor)

@then(u'puedo ver el nombre del proyecto "{nombre_proyecto}" en la lista de proyectos')
def step_impl(context, nombre_proyecto):
    proyectos = context.driver.find_elements(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for proyecto in proyectos:
        if proyecto.find_element(By.XPATH, 'td[1]').text == nombre_proyecto:
            assert True, f"El nombre {nombre_proyecto} no se encuentra en la lista de proyectos"
            