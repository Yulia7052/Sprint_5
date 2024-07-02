from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import consts

def test_constructor_open_filling_tab(driver):
    driver.get(consts.SITE_URL)

    burger_divs = driver.find_elements(By.CLASS_NAME, consts.BURGER_DIVS_CLASS)       

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(burger_divs[consts.FILLING_DIV_INDEX]))
    burger_divs[consts.FILLING_DIV_INDEX].click()
    tab_select_class_attr = burger_divs[consts.FILLING_DIV_INDEX].get_attribute('class')

    assert 'tab_tab_type_current' in tab_select_class_attr
