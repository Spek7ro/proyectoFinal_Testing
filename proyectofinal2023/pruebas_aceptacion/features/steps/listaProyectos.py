from behave import given
from selenium.webdriver.common.by import By


@given(u'le doy clik en el enlace proyectos')
def step_impl(context): context.driver.find_element(
    By.LINK_TEXT, 'Proyectos').click()


@given(u'luego clik en el boton de lista de proyectos')
def step_impl(context):
    context.driver.find_element(
        By.XPATH, '//*[@id="collapseUtilities"]/div/a[1]').click()
