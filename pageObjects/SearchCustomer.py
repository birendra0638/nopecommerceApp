class SearchCustomer:
    text_searchemail_id = "SearchEmail"
    text_searchfirstname_id = "SearchFirstName"
    text_searchlastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    tbl_search_res_xpath = "//table[@id='customers-grid']"
    tbl_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tbl_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.text_searchemail_id).clear()
        self.driver.find_element_by_id(self.text_searchemail_id).send_keys(email)

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.text_searchfirstname_id).clear()
        self.driver.find_element_by_id(self.text_searchfirstname_id).send_keys(firstName)

    def setLastName(self, LastName):
        self.driver.find_element_by_id(self.text_searchlastname_id).clear()
        self.driver.find_element_by_id(self.text_searchlastname_id).send_keys(LastName)

    def clickOnSearchBtn(self):
        self.driver.find_element_by_id(self.btn_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tbl_cols_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.tbl_search_res_xpath)
            emailId = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByFirstName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.tbl_search_res_xpath)
            firstname = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if firstname == name:
                flag = True
                break
        return flag
