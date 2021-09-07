import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("**************Test_SearchCustomerByEmail_004***************")
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword((self.password))
        self.lp.clickLogin()

        self.logger.info("***********Login Successful*********")

        self.logger.info("***************Search Customer Test Begin******************")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubmenu()

        self.logger.info("***************Search Customer Test by Email******************")
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCust.clickOnSearchBtn()
        time.sleep(5)
        status = self.searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.lp.clickLogout()
        self.driver.close()
        self.logger.info("***************Test_SearchCustomerByEmail_004 End******************")
