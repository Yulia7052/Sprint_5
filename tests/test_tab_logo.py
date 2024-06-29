from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_tab_logo(driver):
    driver.get(consts.site_url)

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.constructor_reserve_button)))
    driver.find_element(By.XPATH, consts.constructor_reserve_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.site_logo)))
    driver.find_element(By.XPATH, consts.site_logo).click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

