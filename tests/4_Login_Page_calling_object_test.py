import time
import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import LogoutPage

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/11th_Class_2_3_2019_Automation_POM_Framework/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost/login.do")


    def test_login(self,test_launch_browser):
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_logout(self,test_launch_browser):
        lo=LogoutPage(driver)
        lo.click_on_logout_btn()