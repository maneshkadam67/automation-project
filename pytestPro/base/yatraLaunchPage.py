import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class launchpage():
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait
    def departlocation(self,depart):

        departFrom=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
        departFrom.click()
        departFrom.send_keys(depart)
        departFrom.send_keys(Keys.ENTER)
    def goinTo(self,goingto):
        going_to=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(5)
        going_to.send_keys(goingto)
        going_to.send_keys(Keys.ENTER)








