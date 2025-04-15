from data import const, control_words, find_and_click
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import ConstructorLocators as CL
from locators import PersonalAccountLocators as PAL


class TestExitingFromPersonalAccount:

    def test_exiting_from_personal_account_by_click_button_exit(self, authorized_driver):
        find_and_click(authorized_driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(authorized_driver, PAL.BUTTON_EXITING_FROM_ACCOUNT)
        find_and_click(authorized_driver, HL.LOGO)
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_not_logged_in']
