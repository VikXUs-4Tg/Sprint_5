from data import const, find_and_click
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators as CL


class TestConstructor:

    def test_constructor_focus_on_sauces_section_by_button_click (self, driver):
        find_and_click(driver, CL.RADIOBUTTON_SAUCES)
        WDW(driver, const['wait_timer']).until(EC.element_to_be_clickable(CL.TITLE_SAUCES))
        assert driver.find_element(*CL.SCROLL_BAR_POSITION).find_element(*CL.SCROLL_BAR_SAUCES)

    def test_constructor_focus_on_toppings_section_by_button_click (self, driver):
        find_and_click(driver, CL.RADIOBUTTON_TOPPINGS)
        WDW(driver, const['wait_timer']).until(EC.element_to_be_clickable(CL.TITLE_TOPPINGS))
        assert driver.find_element(*CL.SCROLL_BAR_POSITION).find_element(*CL.SCROLL_BAR_TOPPINGS)

    def test_constructor_focus_on_rolls_section_by_button_click (self, driver):
        find_and_click(driver, CL.RADIOBUTTON_TOPPINGS)
        find_and_click(driver, CL.RADIOBUTTON_ROLLS)
        WDW(driver, const['wait_timer']).until(EC.element_to_be_clickable(CL.TITLE_ROLLS))
        assert driver.find_element(*CL.SCROLL_BAR_POSITION).find_element(*CL.SCROLL_BAR_ROLLS)
