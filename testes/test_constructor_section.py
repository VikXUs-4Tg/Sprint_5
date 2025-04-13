from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
#
#
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#
#driver = webdriver.Chrome(options=chrome_options)
#
#webpage='https://qa-mesto.praktikum-services.ru/'
#driver.get(webpage)
#WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "auth-form__button")))
#assert driver.current_url == f'{webpage}signin'
#
#element = driver.find_element(By.XPATH, ".//img")
#print(element)
#print(element.get_attribute('class'))
#
#driver.find_element(By.ID, "email").send_keys("tester108@test.ru")
#driver.find_element(By.ID, "password").send_keys("108108108")
#driver.find_element(By.CLASS_NAME, "auth-form__button").click()
#WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
#assert driver.find_element(By.CLASS_NAME, "header__logout").text == 'Выйти'
#
#WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, 'IdOfMyElement')))
#time.sleep(10)
#
#element = driver.find_element(By.TAG_NAME, "footer")
#driver.execute_script("arguments[0].scrollIntoView();", element)
#time.sleep(1)
#assert 'Mesto Russia' in element.text
#
#new_cookie_first = {"name": "my_first_cookie", "value": "15"}
#driver.add_cookie(new_cookie_first)
#print(driver.get_cookie("my_first_cookie"))
#driver.delete_cookie("my_first_cookie")
#new_cookie_second = {"name": "my_first_cookie", "value": "25"}
#driver.add_cookie(new_cookie_second)
#print(driver.get_cookie("my_first_cookie"))
#assert driver.get_cookie("my_first_cookie")['value'] == '25'
#
#
#time.sleep(1)
#driver.quit()
