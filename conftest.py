import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdrivermanager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup1(request):
    #driver = webdriver.Chrome("D:\chrome\chromedriver.exe")
    #driver = webdriver.Chrome(executable_path="D:\\chrome\chromedriver.exe")
    driver= webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://in.bookmyshow.com/")
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.wait=wait
    yield
    driver.close()
