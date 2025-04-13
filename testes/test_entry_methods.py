from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import driver
from conftest import authorized_driver


wait_timer = 20
authorized_name = "KirillFedorov19_000@yandex.ru"
authorized_password = "108108108"

class TestEntryToPersonalAccount:

    def test_entry_to_personal_account_by_click_button_personal_account(self, driver):
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
        driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_entry_to_account(self, driver):
        driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
        driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_enter_in_form_of_registration (self, driver):
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
        driver.find_element(By.XPATH, ".//a[@href='/login']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
        driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_entry_to_personal_account_by_click_button_enter_in_password_recovery_form(self, driver):
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//a[@href='/forgot-password']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
        driver.find_element(By.XPATH, ".//a[@href='/login']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(authorized_name)
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(authorized_password)
        driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Оформить заказ"
        driver.quit()





