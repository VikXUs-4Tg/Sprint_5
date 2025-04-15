from data import const, control_words, find_and_click, authorization, registration
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL
from locators import ConstructorLocators as CL


class TestRegistration:

    def test_registration_with_valid_data (self, driver, random_name, random_password):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_REGISTRATION)
        registration(driver, random_name, random_password, ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_REGISTRATION)
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        authorization(driver, random_name, random_password, ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_logged_in']

    def test_abort_registration_with_incorrect_password (self, driver, random_name, random_password):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_REGISTRATION)
        registration(driver, random_name, random_password[:5], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_REGISTRATION)
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        authorization(driver, random_name, random_password[:5], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_LOGIN)
        find_and_click(driver, HL.LOGO)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == control_words['user_is_not_logged_in']

    def test_registration_incorrect_password_flag (self, driver, random_name, random_password):
        find_and_click(driver, HL.BUTTON_TO_PERSONAL_ACCOUNT)
        find_and_click(driver, ARPRWL.BUTTON_PASS_TO_REGISTRATION)
        registration(driver, random_name, random_password[:5], ARPRWL.FIELD_FOR_ENTRY_NAME, ARPRWL.FIELD_FOR_ENTRY_PASSWORD, ARPRWL.BUTTON_TO_REGISTRATION)
        WDW(driver, const['wait_timer']).until(EC.visibility_of_element_located(ARPRWL.FLAG_OF_INCORRECT_PASSWORD))
        assert driver.find_element(*ARPRWL.FLAG_OF_INCORRECT_PASSWORD).get_attribute('innerText') == control_words['flag_of_incorrect_password']
