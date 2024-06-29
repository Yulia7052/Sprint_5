from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_login_from_profile_button(driver):
    driver.get(consts.site_url)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.header_profile_button)))
    driver.find_element(By.XPATH, consts.header_profile_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.login_email_field)))
    email = 'ulia_manaenkova_10_088@google.com'
    password = '123456'
    driver.find_element(By.XPATH, consts.login_email_field).send_keys(email)
    driver.find_element(By.XPATH, consts.login_pass_field).send_keys(password)
    driver.find_element(By.XPATH, consts.login_enter_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.constructor_reserve_button)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
