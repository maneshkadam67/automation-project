import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pytestPro.base.base_driver import BaseDriver
from pytestPro.utilities.utils import Utils


class SeatLayout(BaseDriver):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        #self.wait=wait

    def EnterSeatQuantity(self):
        time.sleep(5)
        seats=self.wait_for_PresenceOf_elements(By.XPATH, "//ul[@id='popQty']//li")
        # seats = self.wait.until(
        #     expected_conditions.presence_of_all_elements_located((By.XPATH, "//ul[@id='popQty']//li")))
        seats[0].click()
        # for seat in seats:
        #     if seat.get_attribute('id') == SeatQuantity:
        #         seat.click()
        #

    def clickProceedButton(self):
        proceed=self.wait_for_element_ToBe_clickable(By.XPATH, "//div[@id='proceed-Qty']")
        # proceed = self.wait.until(
        #     expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='proceed-Qty']")))
        proceed.click()


    def selectSeat(self):
        All_seats=self.wait_for_PresenceOf_elements(By.XPATH,"//div[@class='__block']//table[@class='setmain']//tbody//tr//td//a[@class!='_blocked' and @class='_available']")
        # All_seats = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,
        #                                                                                   "//div[@class='__block']//table[@class='setmain']//tbody//tr//td//a[@class!='_blocked' and @class='_available']")))
        All_seats[0].click()
        seatSelected=self.wait_for_element_ToBe_clickable(By.ID, 'btmcntbook')
        #seatSelected = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'btmcntbook')))
        seatSelected.click()
        time.sleep(10)

        self.driver.execute_script("window.scrollTo(0, 150);")
    def selectTicketType(self):
        ticketType=self.wait_for_PresenceOf_elements(By.XPATH, "//div[@id='TickType']//child::div")
        #ut=Utils()
        #ut.assertItemFromList(ticketType,"shmticket")
        # ticketType = self.wait.until(
        #     expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@id='TickType']//child::div")))
        for tickets in ticketType:
            print(tickets.get_attribute('id'))
            #assert (tickets.get_attribute('id'))=="shmticket"
            if tickets.get_attribute('id') == "shmticket":
                tickets.click()

    def clickProceed(self):
        proceedButton=self.wait_for_element_ToBe_clickable(By.XPATH, "//div[@class='btn-bar fnb-proceed-btn']")
        # proceedButton = self.wait.until(
        #     expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='btn-bar fnb-proceed-btn']")))
        proceedButton.click()
        time.sleep(10)
