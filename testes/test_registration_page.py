from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestRegistration:

    def test_registration_with_valid_data (self, driver, wait_timer):
        driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/register']")))
        driver.find_element(By.XPATH, ".//a[@href='/register']").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")))
        names=driver.find_elements(By.XPATH, ".//input[@name='name']")
        names[0].send_keys("654321")
        names[1].send_keys("123456")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("12345")
        time.sleep(30)
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
        WebDriverWait(driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Войти')]")))

        assert driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Оформить заказ"
        driver.quit()


















# Проверь:
# Успешную регистрацию.
# Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru.
# Минимальный пароль — шесть символов.
# Ошибку для некорректного пароля.
# Напиши функцию, которая генерирует логины. Помни что логин это email.
# Подключи генераторы логина и пароля к тестам.