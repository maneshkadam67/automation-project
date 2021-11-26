import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import ShaadiApiumProject.utilities.CustomeLogger as cl


class BasePage():
    log= cl.customLogger()
    def __init__(self,driver):
        self.driver= driver

    def waitforElement(self,locatorvalue,locatorType):
        element=None
        locatorType = locatorType.lower()

        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def scrollMethod(self):
        self.driver.swipe(600,1634,600,800)

    def SendNewConnection(self):
        SendConnection1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView")
        if SendConnection1.is_displayed():
            SendConnection1.click()
            print("New Connection sent")
        else:
            print("Can not send New connection")

    def NewMatchVerifiedAndClick(self):
        time.sleep(10)
        NewMatch = self.driver.find_element_by_id("com.shaadi.android:id/tv_subtitle")
        time.sleep(10)
        NewMatchCard = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ImageView")
        NewMatchText = NewMatch.get_attribute('text')

        if NewMatch.is_displayed():
            time.sleep(5)
            print("New match is displayed")
            NewMatchCard.click()
        else:
            print("Premium match is not displayed")




