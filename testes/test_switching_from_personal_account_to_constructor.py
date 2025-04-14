from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


class TestTransferToConstructor:

    def test_transfer_to_constructor_from_personal_account_bu_click_logo(self, authorized_driver, wait_timer, button_to_personal_account_in_header,title_assemble_the_burger_in_constructor, title_info_personal_account, logo_in_header):
        authorized_driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_info_personal_account)))
        authorized_driver.find_element(By.XPATH, logo_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH,title_assemble_the_burger_in_constructor)))
        assert authorized_driver.find_element(By.XPATH, title_assemble_the_burger_in_constructor).get_attribute('innerText') == "Соберите бургер"
        authorized_driver.quit()

    def test_transfer_to_constructor_from_personal_account_bu_click_button_constructor(self, authorized_driver, wait_timer, button_to_personal_account_in_header, title_assemble_the_burger_in_constructor, title_info_personal_account, button_to_constructor_in_header):
        authorized_driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_info_personal_account)))
        authorized_driver.find_element(By.XPATH,button_to_constructor_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH,title_assemble_the_burger_in_constructor)))
        assert authorized_driver.find_element(By.XPATH, title_assemble_the_burger_in_constructor).get_attribute('innerText') == "Соберите бургер"
        authorized_driver.quit()
