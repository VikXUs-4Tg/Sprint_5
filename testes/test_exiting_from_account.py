from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestExitingFromPersonalAccount:

    def test_exiting_from_personal_account_by_click_button_exit(self, authorized_driver, wait_timer, button_pass_from_constructor_window_to_personal_account, title_assemble_the_burger_in_constructor, button_place_an_order_in_constructor, logo_in_header, button_login_in_authorization_window, title_info_personal_account):
        authorized_driver.find_element(By.XPATH, button_pass_from_constructor_window_to_personal_account).click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_info_personal_account)))
        authorized_driver.find_element(By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_authorization_window)))
        authorized_driver.find_element(By.XPATH, logo_in_header).click()
        WebDriverWait(authorized_driver, wait_timer).until(expected_conditions.visibility_of_element_located((By.XPATH, title_assemble_the_burger_in_constructor)))
        assert authorized_driver.find_element(By.XPATH, button_place_an_order_in_constructor).get_attribute('innerText') == "Войти в аккаунт"
        authorized_driver.quit()
