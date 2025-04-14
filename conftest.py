import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


webpage = 'https://stellarburgers.nomoreparties.site/'

#=====================================================LOCATORS=======================================================

@pytest.fixture
def field_for_entry_name():
    return f".//input[@name='name']"

@pytest.fixture
def field_for_entry_password():
    return f".//input[@name='Пароль']"

@pytest.fixture
def title_assemble_the_burger_in_constructor():
    return f".//h1[@class='text text_type_main-large mb-5 mt-10']"

@pytest.fixture
def title_info_personal_account():
    return f".//p[@class='Account_text__fZAIn text text_type_main-default']"

@pytest.fixture
def button_to_personal_account_in_header():
    return f".//a[@href='/account']"

@pytest.fixture
def button_login_in_authorization_window():
    return f".//button[contains(text(), 'Войти')]"

@pytest.fixture
def button_place_an_order_in_constructor():
    return f".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"

@pytest.fixture
def logo_in_header():
    return f".//div[@class='AppHeader_header__logo__2D0X2']"

@pytest.fixture
def button_to_constructor_in_header():
    return f".//p[contains(text(), 'Конструктор')]"

@pytest.fixture
def button_exiting_from_account_in_personal_account():
    return f".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"

@pytest.fixture
def button_to_registration_in_authorization_window():
    return f".//a[@href='/register']"

@pytest.fixture
def button_login_in_registration_and_password_recovery_windows():
    return f".//a[@href='/login']"

@pytest.fixture
def button_to_password_recovery_in_authorization_window():
    return f".//a[@href='/forgot-password']"

@pytest.fixture
def button_of_registration_in_registration_window():
    return f".//button[contains(text(), 'Зарегистрироваться')]"

@pytest.fixture
def flag_of_incorrect_password_in_registration_window():
    return f".//p[@class='input__error text_type_main-default']"

@pytest.fixture
def radiobutton_sauces_in_constructor():
    return f".//span[contains(text(), 'Соусы')]"

@pytest.fixture
def radiobutton_toppings_in_constructor():
    return f".//span[contains(text(), 'Начинки')]"

@pytest.fixture
def radiobutton_rolls_in_constructor():
    return f".//span[contains(text(), 'Булки')]"

@pytest.fixture
def title_sauces_in_constructor():
    return f".//h2[contains(text(), 'Соусы')]"

@pytest.fixture
def title_toppings_in_constructor():
    return f".//h2[contains(text(), 'Начинки')]"

@pytest.fixture
def title_rolls_in_constructor():
    return f".//h2[contains(text(), 'Булки')]"

#====================================================================================================================

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
def driver(wait_timer, title_assemble_the_burger_in_constructor):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1024,768')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(webpage)
    WDW(driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
    return driver

@pytest.fixture
def authorized_driver(driver, wait_timer, authorized_name, authorized_password, button_to_personal_account_in_header, button_login_in_authorization_window, title_assemble_the_burger_in_constructor, field_for_entry_name, field_for_entry_password):
    driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
    WDW(driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
    driver.find_element(By.XPATH, field_for_entry_name).send_keys(authorized_name)
    driver.find_element(By.XPATH, field_for_entry_password).send_keys(authorized_password)
    driver.find_element(By.XPATH, button_login_in_authorization_window).click()
    WDW(driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
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




