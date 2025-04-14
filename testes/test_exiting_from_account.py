from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import time


class TestExitingFromPersonalAccount:

    def test_exiting_from_personal_account_by_click_button_exit(self, authorized_driver, wait_timer, button_to_personal_account_in_header, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor, logo_in_header, button_login_in_authorization_window, title_info_personal_account, button_exiting_from_account_in_personal_account):
        authorized_driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_info_personal_account)))
        authorized_driver.find_element(By.XPATH, button_exiting_from_account_in_personal_account).click()
        time.sleep(1)
        authorized_driver.find_element(By.XPATH, logo_in_header).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert authorized_driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Войти в аккаунт"
        authorized_driver.quit()
