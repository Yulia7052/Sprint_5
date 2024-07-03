from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_exit_profile(driver):
    driver.get(consts.SITE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.CONSTRUCTOR_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, consts.CONSTRUCTOR_LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.NAME, consts.LOGIN_EMAIL_FIELD_NAME)))
    driver.find_element(By.NAME, consts.LOGIN_EMAIL_FIELD_NAME).send_keys(consts.MAIN_USER_EMAIL)
    driver.find_element(By.NAME, consts.PASS_FIELD_NAME).send_keys(consts.MAIN_USER_PASS)
    driver.find_element(By.XPATH, consts.LOGIN_ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.HEADER_PROFILE_BUTTON)))
    driver.find_element(By.XPATH, consts.HEADER_PROFILE_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.ACCOUNT_LOGOUT_BUTTON)))
    driver.find_element(By.XPATH, consts.ACCOUNT_LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(consts.SITE_LOGIN_URL))
    assert driver.current_url == consts.SITE_LOGIN_URL