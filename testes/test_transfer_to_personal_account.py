from data import const, control_words, find_and_click
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import PersonalAccountLocators as PAL


class TestTransferToPersonalAccount:

    def test_transfer_to_personal_account_by_click_button_personal_account(self, authorized_driver):
        find_and_click(authorized_driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        assert authorized_driver.find_element(*PAL.TITLE_INFO).get_attribute('innerText') == control_words['lighthouse_in_personal_account']
