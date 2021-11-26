from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="D:/chrome/chromedriver.exe")
    #wait = WebDriverWait(driver,20)
    #driver.get("https://www.yatra.com/")
    driver.get("https://in.bookmyshow.com/")
    driver.maximize_window()
    request.cls.driver=driver
    #request.cls.wait=wait
    yield
    driver.close()