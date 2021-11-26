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
log.info("Launch app")
time.sleep(10)
bp.waitforElement("//android.widget.Button[@text='Login']","xpath").click()
time.sleep(2)
Email = bp.waitforElement("//android.widget.EditText[@text='Mobile No. / Email ID']","xpath")
Email.click()
Email.send_keys("7045617485")

driver.back()
time.sleep(2)
Password=bp.waitforElement("//android.widget.EditText[@text='Password']","xpath")
Password.click()
Password.send_keys("Manish@123")
time.sleep(2)
driver.back()
time.sleep(2)

bp.waitforElement("//android.widget.Button[@text='Login']","xpath").click()
time.sleep(5)

bp.waitforElement("//android.widget.Button[@text='ALLOW']","xpath").click()
'''
UpgradeText=driver.find_element_by_id("com.shaadi.android:id/textView_upgrade_title")
skip = driver.find_element_by_xpath("//android.widget.TextView[@text='SKIP']")
print(UpgradeText.get_attribute('text'))
if UpgradeText.is_displayed():
    skip.click()
else:
    print("Skip is not displayed")

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

driver.swipe(600,900,600,700,300)
time.sleep(5)
NewMatch = driver.find_element_by_id("com.shaadi.android:id/tv_subtitle")
NewMatchCard = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup")
NewMatchText = NewMatch.get_attribute('text')

if NewMatch.is_displayed():
    print("New match is displayed")
    NewMatchCard.click()
else:
    print("Premium match is not displayed")


time.sleep(5)
SendConnection1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView")
if SendConnection1.is_displayed():
    SendConnection1.click()
    print("New Connection sent")
else:
    print("Can not send New connection")
time.sleep(5)
driver.quit()