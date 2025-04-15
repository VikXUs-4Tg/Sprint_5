from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import PersonalAccountLocators as PAL


class TestTransferToPersonalAccount:

    def test_transfer_to_personal_account_by_click_button_personal_account(self, authorized_driver, wait_timer):
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        authorized_driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        assert authorized_driver.find_element(*PAL.TITLE_INFO).get_attribute('innerText') == "В этом разделе вы можете изменить свои персональные данные"
