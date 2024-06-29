from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_constructor_open_bun_tab(driver):
    driver.get(consts.site_url)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.constructor_filling_div)))
    variable_div = driver.find_element(By.XPATH, consts.constructor_filling_div)
    variable_div.click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, consts.constructor_bun_div)))
    bun_div = driver.find_element(By.XPATH, consts.constructor_bun_div)
    bun_div.click()
    tab_select_class_attr = bun_div.get_attribute('class')

    assert 'tab_tab_type_current' in tab_select_class_attr
    driver.quit()
