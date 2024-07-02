from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_registration_failure(driver):
    driver.get(consts.SITE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.HEADER_PROFILE_BUTTON)))
    driver.find_element(By.XPATH, consts.HEADER_PROFILE_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOGIN_REGISTRATION_BUTTON)))
    driver.find_element(By.XPATH, consts.LOGIN_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.NAME, consts.PASS_FIELD_NAME)))
    driver.find_element(By.NAME, consts.PASS_FIELD_NAME).send_keys(consts.INCORRECT_PASS)

    driver.find_element(By.XPATH, consts.REGISTRATION_SUBMIT_BUTTON).click()

    error_class_attr = driver.find_element(By.CLASS_NAME, consts.REGISTRATION_PASS_ERROR_CLASS).get_attribute('class')

    assert consts.REGISTRATION_PASS_ERROR_CLASS in error_class_attr


