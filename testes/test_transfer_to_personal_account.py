from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import driver
from conftest import authorized_driver


wait_timer = 20

class TestTransferToPersonalAccount:

    def test_transfer_to_personal_account_bu_click_button(self, authorized_driver):
        #log_in_to_driver(driver)
        authorized_driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")))
        assert authorized_driver.find_element(By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']").get_attribute('innerText') == "В этом разделе вы можете изменить свои персональные данные"
        authorized_driver.quit()

