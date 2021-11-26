from ShaadiApiumProject.base.BasePage import BasePage
from ShaadiApiumProject.tests.LoginPremiumConnection import driver

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import ShaadiApiumProject.utilities.CustomeLogger as cl

_loginButton="//android.widget.Button[@text='Login']"
_enterEmailPhone="//android.widget.EditText[@text='Mobile No. / Email ID']"
_enterPassword="//android.widget.EditText[@text='Password']"
_clickLogin="//android.widget.Button[@text='Login']"
_clickAllowLocation="//android.widget.Button[@text='ALLOW']"
_clickMyShaadi="com.shaadi.android:id/imgMyShaadi"


class Combine(BasePage):
    def __init__(self,driver):
        super.__init__(driver)
        self.driver=driver

    def clickLoginButton(self):
        driver.find_element_by_xpath(_loginButton).click()

    def enterEmailPhone(self, emailORphone):
        email= driver.find_element_by_xpath(_enterEmailPhone)
        email.click()
        email.send_keys(emailORphone)

    def enterPassword(self, password):
        pass1 = driver.find_element_by_xpath(_enterPassword)
        pass1.click()
        pass1.send_keys(password)

    def clickLogin2(self):
        loginButton2= driver.find_element_by_xpath(_clickLogin)
        loginButton2.click()

    def clickAllow(self):
        Allow= driver.find_element_by_xpath(_clickAllowLocation)
        Allow.click()

    def clickOnMyshaadi(self):
        driver.find_element_by_id(_clickMyShaadi).click()