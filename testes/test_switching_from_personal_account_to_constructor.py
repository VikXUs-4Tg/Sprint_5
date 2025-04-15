from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import ConstructorLocators as CL
from locators import PersonalAccountLocators as PAL


class TestTransferToConstructor:

    def test_transfer_to_constructor_from_personal_account_bu_click_logo(self, authorized_driver, wait_timer):
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        authorized_driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        authorized_driver.find_element(*HL.LOGO).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.TITLE_ASSEMBLE_THE_BURGER).get_attribute('innerText') == "Соберите бургер"

    def test_transfer_to_constructor_from_personal_account_bu_click_button_constructor(self, authorized_driver, wait_timer):
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        authorized_driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(PAL.TITLE_INFO))
        authorized_driver.find_element(*HL.BUTTON_TO_CONSTRUCTOR).click()
        WDW(authorized_driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert authorized_driver.find_element(*CL.TITLE_ASSEMBLE_THE_BURGER).get_attribute('innerText') == "Соберите бургер"
