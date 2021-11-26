import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pytestPro.base.yatraLaunchPage import launchpage


@pytest.mark.usefixtures("setup")
class TestBook():
    def test_booking(self):
        lp=launchpage(self.driver,self.wait)
        lp.departlocation("New Delhi")
        lp.goinTo("Mumbai")
        time.sleep(5)




    # #driver.find_element_by_class_name("input").send_keys('maneshi@fhsdk')
