from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL
from locators import ConstructorLocators as CL

class TestEntryToPersonalAccount:

    def test_entry_to_personal_account_by_click_button_personal_account(self, driver, wait_timer, authorized_name, authorized_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(authorized_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(authorized_password)
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Оформить заказ"

    def test_entry_to_personal_account_by_click_button_entry_to_account(self, driver, wait_timer, authorized_name, authorized_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.BUTTON_PLACE_AN_ORDER))
        driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(authorized_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(authorized_password)
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Оформить заказ"

    def test_entry_to_personal_account_by_click_button_enter_in_form_of_registration (self, driver, wait_timer, authorized_name, authorized_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_REGISTRATION))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_LOGIN))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(authorized_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(authorized_password)
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Оформить заказ"

    def test_entry_to_personal_account_by_click_button_enter_in_password_recovery_form(self, driver, wait_timer, authorized_name, authorized_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_PASSWORD_RECOVERY))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_PASSWORD_RECOVERY).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_LOGIN))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(authorized_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(authorized_password)
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Оформить заказ"
