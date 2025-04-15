from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators as CL
import time

class TestConstructor:

    def test_constructor_focus_on_sauces_section_by_button_click (self, driver, position, wait_timer):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.RADIOBUTTON_SAUCES))
        driver.find_element(*CL.RADIOBUTTON_SAUCES).click()
        time.sleep(2)
        assert driver.find_element(*CL.TITLE_SAUCES).location == position

    def test_constructor_focus_on_toppings_section_by_button_click (self, driver, position, wait_timer):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.RADIOBUTTON_TOPPINGS))
        driver.find_element(*CL.RADIOBUTTON_TOPPINGS).click()
        time.sleep(2)
        assert driver.find_element(*CL.TITLE_TOPPINGS).location == position

    def test_constructor_focus_on_rolls_section_by_button_click (self, driver, position, wait_timer):
        WDW(driver, wait_timer).until(EC.visibility_of_element_located(CL.RADIOBUTTON_TOPPINGS))
        driver.find_element(*CL.RADIOBUTTON_TOPPINGS).click()
        time.sleep(2)
        driver.find_element(*CL.RADIOBUTTON_ROLLS).click()
        time.sleep(2)
        assert driver.find_element(*CL.TITLE_ROLLS).location == position
