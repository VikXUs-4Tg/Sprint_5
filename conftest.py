import pytest
import random
import string
from data import const, find_and_click, authorization
from selenium import webdriver
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL

@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(const['webpage'])
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def authorized_driver(driver):
    find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
    authorization(driver, const['authorized_name'], const['authorized_password'], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
    return driver

@pytest.fixture(scope='function')
def random_name():
    login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
    email_name= ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10)))
    email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
    return f"{login_name}@{email_name}.{email_domain}"

@pytest.fixture(scope='function')
def random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(6, 12)))
    return password

