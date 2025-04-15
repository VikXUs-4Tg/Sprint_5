import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL


webpage = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture
def wait_timer():
    return 20

@pytest.fixture
def authorized_name():
    return "KirillFedorov19_000@yandex.ru"

@pytest.fixture
def authorized_password():
    return "108108108"

@pytest.fixture
def position():
    return {'x': 0, 'y': 244}

@pytest.fixture
def driver(wait_timer):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(webpage)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_driver(driver, wait_timer, authorized_name, authorized_password):
    WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
    driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
    WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
    driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(authorized_name)
    driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(authorized_password)
    driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
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

