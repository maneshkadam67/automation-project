import time

import pytest
import softest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager
from ddt import ddt,data,unpack

from pytestPro.page.SeatLayoutPage import SeatLayout
from pytestPro.page.bookingFlow import book
from pytestPro.page.moviesPage import movie
from pytestPro.page.orderSummaryPage import OrderSummary
from pytestPro.page.showTimesPage import showTime


@pytest.mark.usefixtures("setup")
@ddt
class Test_demos(softest.TestCase):
    @data(("Chennai","Antim: The Final Truth","ORDER SUMMARY"),("Pune","Antim: The Final Truth","ORDER SUMMARY"))
    @unpack
    def test_demo1(self,city,movieName,element):
        bk=book(self.driver)
        m=movie(self.driver)
        sh=showTime(self.driver)
        s=SeatLayout(self.driver)
        os=OrderSummary(self.driver)

        # bk.enterCity("Chennai")
        # bk.click_popup()
        # m.click_movieTab()
        # m.selectMovieCard("Antim: The Final Truth")
        # m.clickBookButton()
        bk.LaunchBMSPage(city)
        m.SelectMovie(movieName)
        sh.clickShowTimes()
        sh.clickOnPopup()
        s.EnterSeatQuantity()
        s.clickProceedButton()
        s.selectSeat()
        s.selectTicketType()
        s.clickProceed()
        # os.EnterEmail("abcd@gmail.com")
        # os.EnterMobileNumber("9999999999")
        # os.clickOnSubmit()
        os.AssertElement(element)





        self.driver.execute_script("window.scrollTo(0, 150);")

    #def test_selectCard(self):

    #def test_clickBookButton(self):

    #def test_clickShowTime(self):

    #def test_seatSelection(self):

    #def test_seatLayout(self):

    #def test_selectTicketType(self):

    #def test_clickProceed(self):

# demo12=demos()
# demo12.demo1()
# demo12.selectCard('Maanaadu')
# demo12.clickBookButton()
# demo12.clickShowTime()
# demo12.seatSelection("pop_1")
# demo12.seatLayout()
# demo12.selectTicketType()
# demo12.clickProceed()
