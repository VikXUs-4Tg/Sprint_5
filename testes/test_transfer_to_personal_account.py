from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransferToPersonalAccount:

    def test_transfer_to_personal_account_by_click_button_personal_account(self, authorized_driver, wait_timer, button_to_personal_account_in_header, title_info_personal_account):
        authorized_driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_info_personal_account)))
        assert authorized_driver.find_element(By.XPATH, title_info_personal_account).get_attribute('innerText') == "В этом разделе вы можете изменить свои персональные данные"
        authorized_driver.quit()
