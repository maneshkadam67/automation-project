import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager

from pytestPro.base.base_driver import BaseDriver


class book(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait=wait

    City_Field = "//input[@placeholder='Search for your city']"
    personlize_popup = "//button[@class='No thanks']"

    def get_City(self):
        return self.wait_for_element_located(By.XPATH, self.City_Field)

    def enterCity(self,location):
        self.get_City().send_keys(location)
        self.get_City().send_keys(Keys.ENTER)

    # def selectLocation(self,Location):
    #     city=self.wait_for_element_located(By.XPATH, "//input[@placeholder='Search for your city']")
    #     #city=self.wait_for_element_located(By.XPATH, "//input[@placeholder='Search for your city']")
    #     # city = self.wait.until(
    #     #     expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for your city']")))
    #     city.send_keys(Location)
    #     city.send_keys(Keys.ENTER)

    def get_popup(self):
        return self.wait_for_element_ToBe_clickable(By.XPATH, self.personlize_popup)

    def click_popup(self):
        self.get_popup().click()

    # def personlizationPopup(self):
    #     popup=self.wait_for_element_ToBe_clickable(By.XPATH, self.personlizationPopup())
    #     #popup = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='No thanks']")))
    #     popup.click()

    def LaunchBMSPage(self,location):
        self.enterCity(location)
        self.click_popup()


















