import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
    # chrome_options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(webpage)
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    return driver

@pytest.fixture
def authorized_driver(driver, wait_timer, authorized_name, authorized_password):
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Войти')]")))
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]").click()
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
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


