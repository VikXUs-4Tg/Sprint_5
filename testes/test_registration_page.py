from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registration_with_valid_data (self, driver, wait_timer, random_name, random_password, button_pass_from_constructor_window_to_personal_account, field_for_entry_name, field_for_entry_password, button_login_in_authorization_window, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor):
        driver.find_element(By.XPATH, button_pass_from_constructor_window_to_personal_account).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/register']")))
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password)
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password)
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Оформить заказ"
        driver.quit()

    def test_abort_registration_with_bad_password (self, driver, wait_timer, random_name, random_password, button_pass_from_constructor_window_to_personal_account, field_for_entry_name, field_for_entry_password, button_login_in_authorization_window, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor, logo_in_header):
        driver.find_element(By.XPATH, button_pass_from_constructor_window_to_personal_account).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/register']")))
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, button_pass_from_constructor_window_to_personal_account).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        driver.find_element(By.XPATH, field_for_entry_name).send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, button_login_in_authorization_window).click()
        driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Войти в аккаунт"
        driver.quit()

    def test_registration_bad_password_flag (self, driver, wait_timer, random_name, random_password, button_pass_from_constructor_window_to_personal_account, field_for_entry_name, field_for_entry_password):
        driver.find_element(By.XPATH, button_pass_from_constructor_window_to_personal_account).click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/register']")))
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")))
        names=driver.find_elements(By.XPATH, field_for_entry_name)
        names[0].send_keys(random_name[:random_name.find('@')])
        names[1].send_keys(random_name)
        driver.find_element(By.XPATH, field_for_entry_password).send_keys(random_password[:5])
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='input__error text_type_main-default']")))
        assert driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").get_attribute('innerText') == "Некорректный пароль"
        driver.quit()


















# Проверь:
# Успешную регистрацию.
# Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru.
# Минимальный пароль — шесть символов.
# Ошибку для некорректного пароля.
# Напиши функцию, которая генерирует логины. Помни что логин это email.
# Подключи генераторы логина и пароля к тестам.