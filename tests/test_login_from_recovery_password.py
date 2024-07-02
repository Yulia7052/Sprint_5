from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_login_from_recovery_password(driver):
    driver.get(consts.SITE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.CONSTRUCTOR_ACCOUNT_LOGIN_BUTTON)))
    driver.find_element(By.XPATH, consts.CONSTRUCTOR_ACCOUNT_LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOGIN_RECOVERY_PASSWORD_BUTTON)))
    driver.find_element(By.XPATH, consts.LOGIN_RECOVERY_PASSWORD_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.LOGIN_BUTTON)))
    driver.find_element(By.XPATH, consts.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.NAME, consts.LOGIN_EMAIL_FIELD_NAME)))
    driver.find_element(By.NAME, consts.LOGIN_EMAIL_FIELD_NAME).send_keys(consts.MAIN_USER_EMAIL)
    driver.find_element(By.NAME, consts.PASS_FIELD_NAME).send_keys(consts.MAIN_USER_PASS)
    driver.find_element(By.XPATH, consts.LOGIN_ENTER_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.HEADER_PROFILE_BUTTON)))
    profile_button_href = driver.find_element(By.XPATH, consts.HEADER_PROFILE_BUTTON).get_attribute('href')
    assert profile_button_href == consts.SITE_ACCOUNT_URL
