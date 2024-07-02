from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_tab_logo(driver):
    driver.get(consts.SITE_URL)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.CONSTRUCTOR_RESERVE_BUTTON)))
    driver.find_element(By.XPATH, consts.CONSTRUCTOR_RESERVE_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.SITE_LOGO)))
    driver.find_element(By.XPATH, consts.CONSTRUCTOR_LOGIN_BUTTON).click()

    assert driver.current_url == consts.SITE_URL