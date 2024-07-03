from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts
import user_generator as generator

def test_registration_new_user(driver):
    driver.get(consts.SITE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.HEADER_PROFILE_BUTTON)))
    driver.find_element(By.XPATH, consts.HEADER_PROFILE_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOGIN_REGISTRATION_BUTTON)))
    driver.find_element(By.XPATH, consts.LOGIN_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.NAME, consts.PASS_FIELD_NAME)))
    
    inputs = driver.find_elements(By.NAME, consts.REGISTRATION_FIELDS_NAME)

    inputs[consts.NAME_INPUT_INDEX].send_keys(consts.NEW_USER_NAME)
    inputs[consts.EMAIL_INPUT_INDEX].send_keys(generator.generate_email())
    driver.find_element(By.NAME, consts.PASS_FIELD_NAME).send_keys(consts.MAIN_USER_PASS)
    driver.find_element(By.XPATH, consts.REGISTRATION_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(consts.SITE_LOGIN_URL))
    assert driver.current_url == consts.SITE_LOGIN_URL


