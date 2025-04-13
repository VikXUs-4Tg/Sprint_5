from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import driver
from conftest import authorized_driver


wait_timer = 20

class TestTransferToConstructor:

    def test_transfer_to_constructor_from_personal_account_bu_click_logo(self, authorized_driver):
        authorized_driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")))
        authorized_driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert authorized_driver.find_element(By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']").get_attribute('innerText') == "Соберите бургер"
        authorized_driver.quit()

    def test_transfer_to_constructor_from_personal_account_bu_click_button_constructor(self, authorized_driver):
        authorized_driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")))
        authorized_driver.find_element(By.XPATH,".//p[contains(text(), 'Конструктор')]").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert authorized_driver.find_element(By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']").get_attribute('innerText') == "Соберите бургер"
        authorized_driver.quit()



