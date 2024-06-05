from behave import given, when
from selenium.webdriver.common.by import By
import time


@given(u'escribo mi nombre de usuario "{username}"')
def step_impl(context, username):
    context.driver.find_element(By.NAME, 'username').send_keys(username)


@given(u'escribo mi nombre "{nombre}"')
def step_impl(context, nombre):
    context.driver.find_element(By.NAME, 'first_name').send_keys(nombre)


@given(u'escribo mi apellido "{apellido}"')
def step_impl(context, apellido):
    context.driver.find_element(By.NAME, 'last_name').send_keys(apellido)


@given(u'escribo mi correo electrónico "{correo}"')
def step_impl(context, correo):
    context.driver.find_element(By.NAME, 'email').send_keys(correo)


@given(u'escribo mi contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, 'password1').send_keys(password)


@given(u'confirmo mi contraseña "{password_confirm}"')
def step_impl(context, password_confirm):
    context.driver.find_element(
        By.NAME, 'password2').send_keys(password_confirm)


@when(u'presiono el botón de Registar')
def step_impl7(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/button').click()
    time.sleep(2)
