from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_PresenceOf_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(expected_conditions.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_for_element_ToBe_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.element_to_be_clickable(
            (locator_type,locator)))
        return element

    def wait_for_element_located(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element=wait.until(expected_conditions.presence_of_element_located((locator_type, locator)))
        return element

#By.XPATH, "//div[contains(@class,'commonStyles__VerticalFlexBox-sc-133848s-2 style__ImageContainer')]"

