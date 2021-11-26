import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("setup1")
class demos():

    def test_demo1(self):
        city = self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for your city']")))
        city.send_keys("Chennai")
        city.send_keys(Keys.ENTER)
        popup = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='No thanks']")))
        popup.click()

        # alert = wait.until(expected_conditions.alert_is_present())
        # alert.accept()

        movie_link = self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Movies")))
        movie_link.click()

        self.driver.execute_script("window.scrollTo(0, 150);")

    def test_selectCard(self):
        cards = self.wait.until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class,'commonStyles__VerticalFlexBox-sc-133848s-2 style__ImageContainer')]")))
        for i in cards:
            # print(i.get_attribute('data-content'))
            if i.get_attribute('data-content') == "Maanaadu":
                i.click()
                break

    def test_clickBookButton(self):
        book_button = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "//div[@class='styles__CtaWrapper-sc-qswwm9-8 JInhj']//div[@class='styles__CtaText-sc-1vmod7e-2 cYhRUm']")))
        book_button.click()

    def test_clickShowTime(self):
        allShowtimes = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,
                                                                                             "//div[@class='showtime-pill-wrapper']//div[@class='showtime-pill-container _filling']//a[@class='showtime-pill']")))
        for times in allShowtimes:
            # print(times.get_attribute('data-showtime-code'))
            if times.get_attribute('data-showtime-code') == "1245":
                times.click()

        # show_time= self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[@class='showtime-pill']")))
        # show_time.click()
        time.sleep(5)
        popup = self.wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='btn-bar']//child::div[@id='btnPopupAccept']")))
        popup.click()

    time.sleep(4)

    def test_seatSelection(self):
        try:
            seats = self.wait.until(
                expected_conditions.presence_of_all_elements_located((By.XPATH, "//ul[@id='popQty']//li")))
            for seat in seats:
                if seat.get_attribute('id') == "pop_1":
                    seat.click()
            proceed = self.wait.until(
                expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='proceed-Qty']")))
            proceed.click()
        except:
            print("Exception thrown")

    def tetst_seatLayout(self):
        All_seats = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,
                                                                                          "//div[@class='__block']//table[@class='setmain']//tbody//tr//td//a[@class!='_blocked' and @class='_available']")))
        All_seats[0].click()
        # for s in All_seats:
        #     print(s)
        #     print(s.get_attribute('onclick'))
        #     #if s.get_attribute('onclick')==seatNumber:
        #    s.click()
        seatSelected = self.wait.until(expected_conditions.element_to_be_clickable((By.ID, 'btmcntbook')))
        seatSelected.click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, 150);")

    def test_selectTicketType(self):
        ticketType = self.wait.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@id='TickType']//child::div")))
        for tickets in ticketType:
            print(tickets.get_attribute('id'))
            if tickets.get_attribute('id') == "shmticket":
                tickets.click()

    def test_clickProceed(self):
        proceedButton = self.wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='btn-bar fnb-proceed-btn']")))
        proceedButton.click()

        time.sleep(10)

# demo12=demos()
# demo12.demo1()
# demo12.selectCard('Maanaadu')
# demo12.clickBookButton()
# demo12.clickShowTime()
# demo12.seatSelection("pop_1")
# demo12.seatLayout()
# demo12.selectTicketType()
# demo12.clickProceed()
