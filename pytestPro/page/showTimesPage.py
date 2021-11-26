import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pytestPro.base.base_driver import BaseDriver


class showTime(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait=wait

    def clickShowTimes(self):
        allShowtimes=self.wait_for_PresenceOf_elements(By.XPATH,"//div[@class='showtime-pill-wrapper']//div[@class='showtime-pill-container']//a[@class='showtime-pill']")
        # allShowtimes = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,
        #                                                                                      "//div[@class='showtime-pill-wrapper']//div[@class='showtime-pill-container']//a[@class='showtime-pill']")))
        allShowtimes[0].click()
        time.sleep(5)
        # for times in allShowtimes:
        #     # print(times.get_attribute('data-showtime-code'))
        #     if times.get_attribute('data-showtime-code') == ShowTime:
        #         times.click()


    def clickOnPopup(self):
        #time.sleep(10)
        popup=self.wait_for_element_ToBe_clickable(By.XPATH, "//div[@id='btnPopupAccept']")
        # popup = self.wait.until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//div[@id='btnPopupAccept']")))
        popup.click()

