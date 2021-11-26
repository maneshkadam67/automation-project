import time

from selenium.webdriver.common.by import By

from pytestPro.base.base_driver import BaseDriver


class OrderSummary(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    Email="//input[@id='txtEmail']"
    Mobile_Number= "//input[@id='txtMobile']"
    Submit="//a[@data-auto='contact-details-continue']"
    Order_susmmary="//div[@id='dOrderSummaryWrap']/h2"

    def get_email(self):
        return self.wait_for_element_located(By.XPATH,self.Email)

    def EnterEmail(self,emailID):
        self.get_email().send_keys(emailID)

    def get_mobile(self):
        return self.wait_for_element_located(By.XPATH,self.Mobile_Number)

    def EnterMobileNumber(self,MobileNo):
        self.get_mobile().send_keys(MobileNo)

    def getSubmit(self):
        return self.wait_for_element_ToBe_clickable(By.XPATH,self.Submit)

    def clickOnSubmit(self):
        self.getSubmit().click()
        time.sleep(10)
    def getOS(self):
        return self.wait_for_element_located(By.XPATH,self.Order_susmmary)

    def AssertElement(self,elementToAssert):
        print(self.getOS().text)
        assert self.getOS().text == elementToAssert
        #print(i.get_attribute('text'))
            #assert i.text()=="ORDER SUMMARY"

