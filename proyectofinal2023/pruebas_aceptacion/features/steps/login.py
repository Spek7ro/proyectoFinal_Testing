from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso a la url "{url}"')
def step_impl1(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'escribo mi usuario "{usuario}" y mi contraseña "{password}"')
def step_impl2(context, usuario, password):
    context.driver.find_element(By.NAME, 'username').send_keys(usuario)
    context.driver.find_element(By.NAME, 'password').send_keys(password)


@when(u'presiono el botón de Ingresar')
def step_impl3(context):
    context.driver.find_element(
        By.XPATH,
        '/html/body/div/div/div/div/div/div/div[2]/div/form/button').click()


@then(u'puedo ver en el banner mi nombre de usuario "{username}"')
def step_impl4(context, username):
    div = context.driver.find_element(By.XPATH, '//*[@id="userDropdown"]/span')
    time.sleep(3)
    assert div.text, f"El {username} no se encuentra en {div.text}"
    time.sleep(1)
