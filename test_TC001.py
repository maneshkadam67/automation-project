import time
from threading import Thread

from appium import webdriver

oDcaps={}
oDcaps['platformName'] = 'Android'
oDcaps['platformVersion'] = '8.0'
oDcaps['deviceName'] = 'HNB4BMYR'
oDcaps['automationName'] = 'UiAutomator2'
#oDcaps['app']= ('D:/Automation project/BMSProject/universal.apk')
oDcaps['appPackage'] = 'com.shaadi.android'
oDcaps['appActivity'] = 'com.shaadi.android.ui.main.MainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',oDcaps)
driver.implicitly_wait(5)
time.sleep(5);

el1 = driver.find_element_by_xpath("//android.widget.Button[@text='Login']")
#el1 = driver.find_element_by_xpath("//android.widget.TextView[@text='Sign Up with Email']")
print("text is",el1.get_attribute('text'))
print("is enabled",el1.is_enabled())
print("is displayed",el1.is_displayed())

el1.click()
time.sleep(10)

        #driver.find_element_by_xpath('//android.widget.TextView[@text="SKIP"]').click()
        #driver.implicitly_wait(5)
        #driver.find_element_by_xpath('//android.widget.Button[@text="ALLOW"]').click()
        #driver.implicitly_wait(5)
        #driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="NEW_NAV_MENU_MOBILE"]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView').click()
        #time.sleep(5)
        #driver.scroll()