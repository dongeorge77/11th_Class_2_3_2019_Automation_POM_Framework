class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_btn_xpath="//*[text()='Logout']"
    def click_on_logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_btn_xpath).click()