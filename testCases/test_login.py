import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# Test_001 is the testcase id


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*********Test_001_Login**********")
        self.logger.info("*********Verifying home Page Title**********")
        # self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("*********Home Page Title test is passed**********")
            self.driver.close()
            assert True
        else:
            self.logger.error("*********Home Page Title test is Failed**********")
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        # self.driver = webdriver.Chrome()
        self.logger.info("********Verifying the Login test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********Login test is passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("*********Login test is Failed **********")
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
