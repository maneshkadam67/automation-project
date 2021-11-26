from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager
#from webdriver_manager.chrome import ChromeDriveManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class demos():
    def demo1(self):
        driver = webdriver.Chrome(executable_path="D:\\chrome\chromedriver.exe")
        #driver.implicitly_wait(10)
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        wait=WebDriverWait(driver,10,2,ignored_exceptions="")
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # time.sleep(4)
        # driver.fullscreen_window()
        ele3=wait.until(expected_conditions.element_to_be_clickable(By.PARTIAL_LINK_TEXT,"Terms of "))
        ele3.click
        # #driver.find_element_by_class_name("input").send_keys('maneshi@fhsdk')
        #driver.find_element_by_css_selector("login-input").send_keys('maneshi@fhsdk')
       # time.sleep(4)
       # driver.find_element_by_partial_link_text("Terms of ").click()
       #  elements=driver.find_elements(By.TAG_NAME, "p")
       #  print("The number of lements",len(elements))
       #  for i in elements:
       #  print(i.get_attribute("value"))

        time.sleep(5)
        # print("Current url",driver.current_url)
        # print("Title is", driver.title)
        #
        # ele1=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        # print("Button is displayed",ele1.is_displayed())
        # print("Button is displayed", ele1.is_enabled())
        # time.sleep(4)
        # dropdown = driver.find_element(By.ID,"UserTitle-Btsh")
        # dd=Select(dropdown)
        # time.sleep(4)
        # dd.select_by_value("Customer_Service_Manager_AP")
        # time.sleep(5)
        # dd.select_by_index(5)
        # ele2=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        # ele2.click()
        # ele2.send_keys("New Delhi")
        # time.sleep(5)
        # ele2.send_keys(Keys.ENTER)
        # print("selected")
        # dem1 = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        # #dem1.screenshot(".\\test1.png")
        # driver.get_screenshot_as_file("D:\\chrome\\test2.png")
        # driver.save_screenshot(".\\test2.png")
        # dem1.click()
        # time.sleep(5)
        # # allDates= driver.find_elements(By.XPATH,"inActiveTD")
        # for dates in allDates:
        #     if dates.get_attribute("data-date") == "17/11/2021":
        #         dates.click()
        #
        #         break

        # driver.find_element(By.XPATH,"//a[@title='Web Check-in']//img[@class='conta iner large-banner']").click()
        # parent_window = driver.current_window_handle
        # print(parent_window)
        # time.sleep(8)
        # handles= driver.window_handles
        # for i in handles:
        #     if i != parent_window:
        #         driver.switch_to_window(handles)
        #         driver.find_element(By.XPATH, "//a[@href='https://www.goindigo.in/how-to-check-in.html?linkNav=how-to-check-in_header']").click()
        more=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        AC=ActionChains(driver)
        AC.move_to_element(more).perform()
        time.sleep(5)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()

        time.sleep(5)












demo11 = demos()
demo11.demo1()

