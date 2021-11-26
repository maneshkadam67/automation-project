import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager

from test_NewTest import demos


@pytest.mark.usefixtures("setup1")
class test1():

    def test_booking(self):
        driver = webdriver.Chrome('D:\chrome\chromedriver.exe')
        wait = WebDriverWait(driver, 10)
        driver.get("https://in.bookmyshow.com/")
        driver.maximize_window()
        demo12 = demos()
        demo12.demo1()
        demo12.selectCard('Maanaadu')
        demo12.clickBookButton()
        demo12.clickShowTime()
        demo12.seatSelection("pop_1")
        demo12.seatLayout()
        demo12.selectTicketType()
        demo12.clickProceed()
