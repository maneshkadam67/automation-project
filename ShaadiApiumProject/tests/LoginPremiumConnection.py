import time

from ShaadiApiumProject.base.DriverClass import Driver
import ShaadiApiumProject.utilities.CustomeLogger as cl
from ShaadiApiumProject.base.BasePage import BasePage
#from ShaadiApiumProject.pages.AllPages import Combine
#import ShaadiApiumProject.pages.AllPages.Combine as cb

driver1=Driver()
log= cl.customLogger()
driver = driver1.getDriverFunction()
bp= BasePage(driver)
#cb=Combine(driver)
log.info("Launch app")
time.sleep(10)
bp.waitforElement("//android.widget.Button[@text='Login']","xpath").click()
#cb.clickLoginButton()
time.sleep(2)
Email = bp.waitforElement("//android.widget.EditText[@text='Mobile No. / Email ID']","xpath")
Email.click()
Email.send_keys("maneshkadam67@gmail.com")
#cb.enterEmailPhone("maneshkadam67@gmail.com")
driver.back()
time.sleep(2)
#cb.enterPassword("Manish@123")
Password=bp.waitforElement("//android.widget.EditText[@text='Password']","xpath")
Password.click()
Password.send_keys("Manish@123")
time.sleep(2)
driver.back()
time.sleep(2)

bp.waitforElement("//android.widget.Button[@text='Login']","xpath").click()
time.sleep(2)

bp.waitforElement("//android.widget.Button[@text='ALLOW']","xpath").click()

'''
skip = bp.waitforElement("//android.widget.TextView[@text='SKIP']","xpath")
try:
    if skip.is_displayed():
        time.sleep(5)
        skip.click()

    else:
        print("Skip button not displayed")
except:
    print("Exception raised")
'''

time.sleep(2)
bp.waitforElement("com.shaadi.android:id/imgMyShaadi","id").click()
time.sleep(6)

driver.swipe(600,800,600,1200,300)
time.sleep(5)
PremiumMatch= driver.find_element_by_id("com.shaadi.android:id/tv_title")
PremiumMatchCard= driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ImageView")
premiumText=PremiumMatch.get_attribute('text')
#SendConnection1= driver.find_element_by_id("com.shaadi.android:id/btnConnect")

if PremiumMatch.is_displayed():
    print("Premium match is displayed")
    PremiumMatchCard.click()
else:
    print("Premium match is not displayed")
time.sleep(5)

sendConnect=driver.find_element_by_id("com.shaadi.android:id/button_main_tick")

if sendConnect.is_displayed():
    sendConnect.click()
    print("Premium Connection sent")
else:
    print("Can not send connection")
time.sleep(5)
driver.quit()

