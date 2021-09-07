import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Xutils


# Test_001 is the testcase id


@pytest.mark.regression
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURl()
    path = ".//testData//Logindata.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("********Test_001_DDT_Login***********")
        self.logger.info("********Verifying the Login DDT test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.rows = Xutils.getRowCount(self.path, 'dataTable')
        print("Number of rows in excel:", self.rows)
        lst_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            self.user = Xutils.readData(self.path, "dataTable", r, 1)
            self.password = Xutils.readData(self.path, "dataTable", r, 2)
            self.exp = Xutils.readData(self.path, "dataTable", r, 3)

            print(self.user, self.password, self.exp)
            self.lp.setUserName(self.user)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print("act_title:", act_title)
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                print("self.exp is", self.exp)
                if self.exp == "Pass":
                    self.logger.info("********* passed **********")
                    self.lp.clickLogout()
                    lst_status.append("pass")

                elif self.exp == "Fail":
                    self.logger.error("********* Failed **********")
                    self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***** Failed*****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** Passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.error("*****Login DDT test Failed*******")
            self.driver.close()
            assert False
        self.logger.info("***********End of Login DDT Test ********")
        self.logger.info("**********Completed Test_002_DDT_Login*************");
