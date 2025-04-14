from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestRegistration:

    def test_registration_with_valid_data (self, driver, wait_timer, random_name, random_password, button_to_personal_account_in_header, field_for_entry_name, field_for_entry_password, button_login_in_authorization_window, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor, button_to_registration_in_authorization_window, button_of_registration_in_registration_window, logo_in_header):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_to_registration_in_authorization_window)))
        driver.find_element(By.XPATH, button_to_registration_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_of_registration_in_registration_window)))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password)
        driver.find_element(By.XPATH, button_of_registration_in_registration_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_abort_registration_with_incorrect_password (self, driver, wait_timer, random_name, random_password, button_to_personal_account_in_header, field_for_entry_name, field_for_entry_password, button_login_in_authorization_window, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor, logo_in_header, button_to_registration_in_authorization_window, button_of_registration_in_registration_window):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_to_registration_in_authorization_window)))
        driver.find_element(By.XPATH, button_to_registration_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_of_registration_in_registration_window)))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, button_of_registration_in_registration_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        time.sleep(1)
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Войти в аккаунт"
        driver.quit()

    def test_registration_incorrect_password_flag (self, driver, wait_timer, random_name, random_password, button_to_personal_account_in_header, field_for_entry_name, field_for_entry_password, button_to_registration_in_authorization_window, button_of_registration_in_registration_window, flag_of_incorrect_password_in_registration_window):
        driver.find_element(By.XPATH, button_to_personal_account_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_to_registration_in_authorization_window)))
        driver.find_element(By.XPATH, button_to_registration_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_of_registration_in_registration_window)))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, button_of_registration_in_registration_window).click()
        time.sleep(1)
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, flag_of_incorrect_password_in_registration_window)))
        assert driver.find_element(By.XPATH, flag_of_incorrect_password_in_registration_window).get_attribute('innerText') == "Некорректный пароль"
        driver.quit()
