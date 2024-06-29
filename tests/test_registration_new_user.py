from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_registration_new_user(driver):
    driver.get(consts.site_url)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.header_profile_button)))
    driver.find_element(By.XPATH, consts.header_profile_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.login_registration_button)))
    driver.find_element(By.XPATH, consts.login_registration_button).click()

    name = 'Персик Яблочный'
    email = 'ulia_manaenkova_10_025@ya.ru'
    password = '653412'
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, consts.registration_name_field)))
    driver.find_element(By.XPATH, consts.registration_name_field).send_keys(name)
    driver.find_element(By.XPATH, consts.registration_email_field).send_keys(email)
    driver.find_element(By.XPATH, consts.registration_pass_field).send_keys(password)
    driver.find_element(By.XPATH, consts.registration_submit_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


