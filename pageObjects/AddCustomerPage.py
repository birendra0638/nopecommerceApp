import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customers_menu_xpath = "//p[contains(text(),'Customers')]"
    link_customers_Submenu_xpath = "//a[@href='/Admin/Customer/List']//p[text()=' Customers']"
    btn_addnew_xpath = "//a[@class='btn btn-primary']"
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_firstname_xpath = "//input[@id='FirstName']"
    text_lastname_xpath = "//input[@id='LastName']"
    rad_male_gender_id = "Gender_Male"
    rad_female_gender_id = "Gender_Female"
    datepicker_dob_id = "DateOfBirth"
    txt_companyname_id = "Company"
    chkbox_istaxexempt_id = "IsTaxExempt"
    txt_newsletter_id = "SelectedNewsletterSubscriptionStoreIds_label"

    lstCustomerrole_xpath = "//div[div[label[contains(text(),'Customer roles')]]]/following-sibling::div/div/div/div/div"
    lstrole_del_regd_xpath = "//span[@title='delete']"
    lstrole_administered_xpath = "//li[text()='Administrators']"
    lstrole_guests_xpath = "//li[text()='Guests']"
    lstrole_registered_xpath = "//li[text()='Registered']"
    lstrole_moderator_xpath = "//li[text()='Forum Moderators']"
    lstrole_vendors_xpath = "//li[text()='Vendors']"

    drpmng_vendor_id = "VendorId"
    txt_admincomment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.link_customers_menu_xpath).click()

    def clickOnCustomerSubmenu(self):
        self.driver.find_element_by_xpath(self.link_customers_Submenu_xpath).click()

    def clickOnAddNewBtn(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.text_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.text_firstname_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_xpath(self.text_lastname_xpath).send_keys(lastName)

    def setGender(self):
        self.driver.find_element_by_id(self.rad_male_gender_id).click()

    def setDob(self, date):
        self.driver.find_element_by_id(self.datepicker_dob_id).send_keys(date)

    def setCompanyName(self, companyName):
        self.driver.find_element_by_id(self.txt_companyname_id).send_keys(companyName)

    def setTaxExempt(self):
        self.driver.find_element_by_id(self.chkbox_istaxexempt_id).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.lstCustomerrole_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_registered_xpath)

        elif role == 'Administrators':
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_administered_xpath)

        elif role == 'Forum Moderators':
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_moderator_xpath)

        elif role == 'Guests':
            self.driver.find_element_by_xpath(self.lstrole_del_regd_xpath).click()
            time.sleep(2)
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_guests_xpath)

        elif role == 'Vendors':
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_vendors_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self.lstrole_guests_xpath)

        self.listItem.click()

    def setVendor(self, value):
        drp_mgOfVendor = self.driver.find_element_by_id(self.drpmng_vendor_id)
        selDrp = Select(drp_mgOfVendor)
        selDrp.select_by_value(value)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.txt_admincomment_xpath).send_keys(comment)

    def clickOnSaveBtn(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    def captureSucMsg(self):
        self.msg = self.driver.find_element_by_tag_name("body")

