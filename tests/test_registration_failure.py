from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_registration_failure(driver):
    driver.get(consts.site_url)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.header_profile_button)))
    driver.find_element(By.XPATH, consts.header_profile_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.login_registration_button)))
    driver.find_element(By.XPATH, consts.login_registration_button).click()

    password = '123'
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.registration_pass_field)))
    driver.find_element(By.XPATH, consts.registration_pass_field).send_keys(password)

    driver.find_element(By.XPATH, consts.registration_submit_button).click()

    error_class_attr = driver.find_element(By.XPATH, consts.registration_pass_div).get_attribute('class')

    assert 'input_status_error' in error_class_attr
    driver.quit()


