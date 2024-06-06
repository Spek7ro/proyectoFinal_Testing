from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given(u'presiono el botón de Ingresar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH,
        '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@given(u'le doy clik en el enlace proveedores')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Proveedores').click()


@given(u'luego clik en el boton de Agregar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseTwo"]/div/a[2]').click()


@given(u'escribo el RFC del proveedor "{rfc}"')
def step_impl(context, rfc):
    context.driver.find_element(By.NAME, 'rfc').send_keys(rfc)


@given(u'escribo la razon social del proveedor "{razon_social}"')
def step_impl(context, razon_social):
    context.driver.find_element(
        By.NAME, 'razon_social').send_keys(razon_social)


@given(u'escribo la dirección del proveedor "{direccion}"')
def step_impl(context, direccion):
    context.driver.find_element(By.NAME, 'direccion').send_keys(direccion)


@given(u'escribo el telefono del proveedor "{telefono}"')
def step_impl(context, telefono):
    context.driver.find_element(By.NAME, 'telefono').send_keys(telefono)


@given(u'escribo el correo del proveedor "{correo}"')
def step_impl(context, correo):
    context.driver.find_element(By.NAME, 'correo').send_keys(correo)


@given(u'selecciono el estado del proveedor "{estado}"')
def step_impl(context, estado):
    context.driver.find_element(By.NAME, 'estado').send_keys(estado)


@given(u'selecciono el municipio del proveedor "{municipio}"')
def step_impl(context, municipio):
    context.driver.find_element(By.NAME, 'municipio').send_keys(municipio)


@when(u'presiono el boton Agregar')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="content"]/div/div/div/form/button').click()


@then(u'puedo ver el RFC del proveedor "{rfc}" en la lista de proveedores')
def step_impl(context, rfc):
    proveedores = context.driver.find_elements(
        By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div/div[1]/table/tbody/tr')
    for proveedor in proveedores:
        if proveedor.find_element(By.XPATH, 'td[1]').text == rfc:
            assert True, f"El RFC {
                rfc} no se encuentra en la lista de proveedores"
    time.sleep(3)
