from selenium.webdriver.common.by import By
import time


class TestConstructor:

    def test_constructor_focus_on_sauces_section_by_button_click (self, driver, position, radiobutton_sauces_in_constructor, title_sauces_in_constructor):
        driver.find_element(By.XPATH, radiobutton_sauces_in_constructor).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, title_sauces_in_constructor).location == position
        driver.quit()

    def test_constructor_focus_on_toppings_section_by_button_click (self, driver, position, radiobutton_toppings_in_constructor, title_toppings_in_constructor):
        driver.find_element(By.XPATH, radiobutton_toppings_in_constructor).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, title_toppings_in_constructor).location == position
        driver.quit()

    def test_constructor_focus_on_rolls_section_by_button_click (self, driver, position, radiobutton_toppings_in_constructor, radiobutton_rolls_in_constructor, title_rolls_in_constructor):
        driver.find_element(By.XPATH, radiobutton_toppings_in_constructor).click()
        time.sleep(2)
        driver.find_element(By.XPATH, radiobutton_rolls_in_constructor).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, title_rolls_in_constructor).location == position
        driver.quit()
