from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class TestEntryToPersonalAccount:

    def test_entry_to_personal_account_by_click_button_personal_account(self, driver, wait_timer, authorized_name, authorized_password, logo_in_header, button_login_in_authorization_window, button_place_an_order_in_constructor, title_assemble_the_burger_in_constructor, field_for_entry_name, field_for_entry_password, button_to_personal_account_in_header):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(authorized_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(authorized_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_entry_to_account(self, driver, wait_timer, authorized_name, authorized_password, logo_in_header, button_login_in_authorization_window, button_place_an_order_in_constructor, title_assemble_the_burger_in_constructor, field_for_entry_name, field_for_entry_password):
        driver.find_element(By.XPATH, button_place_an_order_in_constructor).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(authorized_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(authorized_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_enter_in_form_of_registration (self, driver, wait_timer, authorized_name, authorized_password, logo_in_header, button_login_in_authorization_window, button_place_an_order_in_constructor, title_assemble_the_burger_in_constructor, field_for_entry_name, field_for_entry_password, button_to_personal_account_in_header, button_login_in_registration_and_password_recovery_windows, button_to_registration_in_authorization_window):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, button_to_registration_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_registration_and_password_recovery_windows)))
        driver.find_element(By.XPATH, button_login_in_registration_and_password_recovery_windows).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(authorized_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(authorized_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_enter_in_password_recovery_form(self, driver, wait_timer, authorized_name, authorized_password, logo_in_header, button_login_in_authorization_window, button_place_an_order_in_constructor, title_assemble_the_burger_in_constructor, field_for_entry_name, field_for_entry_password, button_to_personal_account_in_header, button_login_in_registration_and_password_recovery_windows, button_to_password_recovery_in_authorization_window):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, button_to_password_recovery_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_registration_and_password_recovery_windows)))
        driver.find_element(By.XPATH, button_login_in_registration_and_password_recovery_windows).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(authorized_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(authorized_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()
