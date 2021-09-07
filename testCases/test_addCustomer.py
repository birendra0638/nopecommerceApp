import pytest
import pytest_html
import random
import string
import time
from selenium import webdriver
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURl()
    userName = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("**************Test_003_AddCustomer***************")
        self.logger.info("**************User login initiated****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***********Login Successful*********")

        self.logger.info("***************Add Customer Test Begin******************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubmenu()
        self.addCust.clickOnAddNewBtn()

        self.logger.info("***************Adding customer Info******************")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("B!ndhani2021")
        self.addCust.setFirstName("Bikash")
        self.addCust.setLastName("Jena")
        self.addCust.setGender()
        self.addCust.setDob("3/1/1994")
        self.addCust.setCompanyName("QACompany")
        self.addCust.setTaxExempt()
        self.addCust.setCustomerRoles("Administrators")
        # self.addCust.setVendor("2")
        self.addCust.setAdminComment("This is for testing.........")
        self.addCust.clickOnSaveBtn()
        time.sleep(5)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer test validation passed *****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "AddCustomer_scr_001.png")
            self.logger.error("********* Add customer test validation Failed *****************")
            assert False
        self.driver.close()
        self.logger.info("***************Add Customer Test End******************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
