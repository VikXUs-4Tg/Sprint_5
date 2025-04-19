from data import const, control_words, find_and_click
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import ConstructorLocators as CL
from locators import PersonalAccountLocators as PAL


class TestTransferToConstructor:

    def test_transfer_to_constructor_from_personal_account_bu_click_logo(self, authorized_driver):
        find_and_click(authorized_driver,HL.BUTTON_TO_PERSONAL_ACCOUNT)
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        authorized_driver.find_element(*HL.LOGO).click()
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.TITLE_ASSEMBLE_THE_BURGER).get_attribute('innerText') == control_words['lighthouse_in_constructor']

    def test_transfer_to_constructor_from_personal_account_bu_click_button_constructor(self, authorized_driver):
        find_and_click(authorized_driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        authorized_driver.find_element(*HL.BUTTON_TO_CONSTRUCTOR).click()
        WDW(authorized_driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.TITLE_ASSEMBLE_THE_BURGER).get_attribute('innerText') == control_words['lighthouse_in_constructor']
