from data import const, control_words, find_and_click, authorization
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL
from locators import ConstructorLocators as CL


class TestEntryToPersonalAccount:

    def test_entry_to_personal_account_by_click_button_personal_account(self, driver):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        authorization(driver, const['authorized_name'], const['authorized_password'], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_logged_in']

    def test_entry_to_personal_account_by_click_button_entry_to_account(self, driver):
        find_and_click(driver, CL.BUTTON_PLACE_AN_ORDER)
        authorization(driver, const['authorized_name'], const['authorized_password'], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_logged_in']

    def test_entry_to_personal_account_by_click_button_enter_in_form_of_registration (self, driver):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_REGISTRATION)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_LOGIN)
        authorization(driver, const['authorized_name'], const['authorized_password'], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_logged_in']

    def test_entry_to_personal_account_by_click_button_enter_in_password_recovery_form(self, driver):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_PASSWORD_RECOVERY)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_LOGIN)
        authorization(driver, const['authorized_name'], const['authorized_password'], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_logged_in']
