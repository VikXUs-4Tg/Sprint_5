from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators as HL
from locators import AuthorizationRegistrationAndPasswordRecoveryWindowsLocators as ARPRWL
from locators import ConstructorLocators as CL


class TestRegistration:

    def test_registration_with_valid_data (self, driver, wait_timer, random_name, random_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_REGISTRATION))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_REGISTRATION))
        names=driver.find_elements(*ARPRWL.FIELD_FOR_ENTRY_NAME)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(random_password)
        driver.find_element(*ARPRWL.BUTTON_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(random_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(random_password)
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Оформить заказ"

    def test_abort_registration_with_incorrect_password (self, driver, wait_timer, random_name, random_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_REGISTRATION))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_REGISTRATION))
        names = driver.find_elements(*ARPRWL.FIELD_FOR_ENTRY_NAME)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(random_password[:5])
        driver.find_element(*ARPRWL.BUTTON_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_LOGIN))
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_NAME).send_keys(random_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(random_password[:5])
        driver.find_element(*ARPRWL.BUTTON_TO_LOGIN).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.LOGO))
        driver.find_element(*HL.LOGO).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.TITLE_ASSEMBLE_THE_BURGER))
        assert driver.find_element(*CL.BUTTON_PLACE_AN_ORDER).get_attribute('innerText') == "Войти в аккаунт"

    def test_registration_incorrect_password_flag (self, driver, wait_timer, random_name, random_password):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(HL.BUTTON_TO_PERSONAL_ACCOUNT))
        driver.find_element(*HL.BUTTON_TO_PERSONAL_ACCOUNT).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_PASS_TO_REGISTRATION))
        driver.find_element(*ARPRWL.BUTTON_PASS_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.BUTTON_TO_REGISTRATION))
        names = driver.find_elements(*ARPRWL.FIELD_FOR_ENTRY_NAME)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(*ARPRWL.FIELD_FOR_ENTRY_PASSWORD).send_keys(random_password[:5])
        driver.find_element(*ARPRWL.BUTTON_TO_REGISTRATION).click()
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(ARPRWL.FLAG_OF_INCORRECT_PASSWORD))
        assert driver.find_element(*ARPRWL.FLAG_OF_INCORRECT_PASSWORD).get_attribute('innerText') == "Некорректный пароль"
