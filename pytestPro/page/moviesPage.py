import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pytestPro.base.base_driver import BaseDriver
from pytestPro.utilities.utils import Utils


class movie(BaseDriver):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)


    #Locators
    movie_tab = "Movies"
    cards_list = "//div[@class='sc-dv5ht7-0 eQcIov']//div[2]"
    book_button = "//div[@id='super-container']//div//section//div//div//div//div//div[@id='page-cta-container']//button[@data-phase='postRelease']//div//span[contains(text(),'Book tickets')]"

    def get_movieTab(self):
        return self.wait_for_element_ToBe_clickable(By.LINK_TEXT, self.movie_tab)

    def click_movieTab(self):
        self.get_movieTab().click()
        self.driver.execute_script("window.scrollTo(0, 150);")

        #self.wait=wait
    # def clickMovieTab(self):
    #     movie_link=self.wait_for_element_ToBe_clickable(By.LINK_TEXT, "Movies")
    #
    #     #movie_link = self.wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Movies")))
    #     movie_link.click()
    #     self.driver.execute_script("window.scrollTo(0, 150);")

    def getCards(self):
        return self.wait_for_PresenceOf_elements(By.XPATH, self.cards_list)

    def selectMovieCard(self, movieName):
        for i in self.getCards():
            #cards[0].click()
            if i.get_attribute('data-content') == movieName:
                i.click()
                break



    # def selectMovieCard(self,movieName):
    #
    #     cards=self.wait_for_PresenceOf_elements(By.XPATH,"//div[@class='sc-dv5ht7-0 eQcIov']//div[2]")
    #     #cards=self.wait_for_PresenceOf_elements(By.XPATH,"//div[contains(@class,'commonStyles__VerticalFlexBox-sc-133848s-2 style__ImageContainer')]")
    #     #print(len(cards))
    #     #cards = self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, )))
    #     for i in cards:
    #         #cards[0].click()
    #         if i.get_attribute('data-content') == movieName:
    #             i.click()
    #             break
    def getBookButton(self):
        return self.wait_for_element_ToBe_clickable(By.XPATH,self.book_button)

    def clickBookButton(self):
        self.getBookButton().click()

    # def clickBookButton(self):
    #     #book_button = self.wait_for_element_ToBe_clickable((By.XPATH,"//div[@class='styles__CtaWrapper-sc-qswwm9-8 JInhj']//div[@class='styles__CtaText-sc-1vmod7e-2 cYhRUm']")))
    #     book_button=self.wait_for_element_ToBe_clickable(By.XPATH,"//div[@id='super-container']//div//section//div//div//div//div//div[@id='page-cta-container']//button[@data-phase='postRelease']//div//span[contains(text(),'Book tickets')]")
    #     book_button.click()
    #     time.sleep(5)
    def SelectMovie(self,movieName):
        self.click_movieTab()
        self.selectMovieCard(movieName)
        self.clickBookButton()


