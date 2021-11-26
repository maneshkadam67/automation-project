from datetime import time

from appium import webdriver

class Driver:
    def getDriverFunction(self):
        oDcaps={}
        oDcaps['platformName'] = 'Android'
        oDcaps['platformVersion'] = '8.0'
        oDcaps['deviceName'] = 'HNB4BMYR'
        #oDcaps['deviceName'] = 'EI4LCIK7OJMBPVNZ'
        oDcaps['automationName'] = 'UiAutomator2'
        oDcaps['appPackage'] = 'com.shaadi.android'
        oDcaps['appActivity'] = 'com.shaadi.android.ui.main.MainActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',oDcaps)
        return driver
