from selenium.webdriver.common.by import By
import time


class TestConstructor:

    def test_constructor_focus_on_sauces_section_by_button_click (self, driver, position):
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, ".//h2[contains(text(), 'Соусы')]").location == position
        driver.quit()

    def test_constructor_focus_on_toppings_section_by_button_click (self, driver, position):
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, ".//h2[contains(text(), 'Начинки')]").location == position
        driver.quit()

    def test_constructor_focus_on_rolls_section_by_button_click (self, driver, position):
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Булки')]").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, ".//h2[contains(text(), 'Булки')]").location == position
        driver.quit()
