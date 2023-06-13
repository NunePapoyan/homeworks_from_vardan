import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    def test_signin(self):
        usernameFieldElement = self.driver.find_element(By.ID, "ap_email")
        usernameFieldElement.clear()
        usernameFieldElement.send_keys("nunetest7@gmail.com")
        usernameFieldElement.send_keys(Keys.ENTER)
        time.sleep(2)

        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.send_keys("Test1324")
        keepFieldElement = self.driver.find_element(By.NAME, "rememberMe")
        keepFieldElement.click()
        time.sleep(5)
        signinFieldElement = self.driver.find_element(By.ID, "auth-signin-button")
        signinFieldElement.click()
        time.sleep(5)

        searchFieldElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFieldElement.click()
        searchFieldElement.send_keys("Watch")
        searchFieldButton = self.driver.find_element(By.ID, "nav-search-submit-text")
        searchFieldButton.click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,100)","")

        productFieldElement = self.driver.find_element(By.XPATH,
                                                  '(//div[@class="a-section aok-relative s-image-square-aspect"])[2]')
        productFieldElement.click()
        time.sleep(3)

        addCardFieldElement = self.driver.find_element(By.ID, "submit.add-to-cart")
        addCardFieldElement.click()
        cardFieldElement = self.driver.find_element(By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")
        addCardFieldText =  cardFieldElement.text
        time.sleep(5)


        assert addCardFieldText == "Added to Cart"
        assert self.driver.title == "Amazon.com Shopping Card"

def tearDown(self):
    self.driver.close()


