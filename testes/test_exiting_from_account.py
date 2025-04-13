from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestExitingFromPersonalAccount:

    def test_exiting_from_personal_account_by_click_button_exit(self, authorized_driver, wait_timer):
        authorized_driver.find_element(By.XPATH, ".//a[@href='/account']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']")))
        authorized_driver.find_element(By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))
        authorized_driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']")))
        assert authorized_driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").get_attribute('innerText') == "Войти в аккаунт"
        authorized_driver.quit()
