import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
#import time

wait_timer = 20
authorized_name = "KirillFedorov19_000@yandex.ru"
authorized_password = "108108108"

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    webpage = 'https://stellarburgers.nomoreparties.site/'
    driver.get(webpage)
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    return driver

@pytest.fixture
def authorized_driver(driver):
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
    driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
    driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))
    return driver