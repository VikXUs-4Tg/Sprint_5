from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import ConstructorLocators as CL
from locators import PersonalAccountLocators as PAL


class TestExitingFromPersonalAccount:

    def test_exiting_from_personal_account_by_click_button_exit(self, authorized_driver, wait_timer):
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        authorized_driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(PAL.BUTTON_EXITING_FROM_ACCOUNT))
        authorized_driver.find_element(*PAL.BUTTON_EXITING_FROM_ACCOUNT).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        authorized_driver.find_element(*HL.LOGO).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Войти в аккаунт"
