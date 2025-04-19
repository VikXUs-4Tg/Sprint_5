from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

def find_and_click(driver, element):
    WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(element))
    driver.find_element(*element).click()

def authorization(driver, login, password, login_field, password_field, button):
    WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(button))
    driver.find_element(*login_field).send_keys(login)
    driver.find_element(*password_field).send_keys(password)
    driver.find_element(*button).click()

def registration(driver, login, password, login_field, password_field, button):
    WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(button))
    names = driver.find_elements(*login_field)
    names[0].send_keys(login[:login.find('@')])
    names[1].send_keys(login)
    driver.find_element(*password_field).send_keys(password)
    driver.find_element(*button).click()

const = {
'webpage' : 'https://stellarburgers.nomoreparties.site/',
'wait_timer' : 20,
'authorized_name' : 'KirillFedorov19_000@yandex.ru',
'authorized_password' : '108108108'
}

control_words = {
'user_is_logged_in' : 'Оформить заказ',
'user_is_not_logged_in' : 'Войти в аккаунт',
'flag_of_incorrect_password' : 'Некорректный пароль',
'lighthouse_in_constructor' : 'Соберите бургер',
'lighthouse_in_personal_account' : 'В этом разделе вы можете изменить свои персональные данные'
}
