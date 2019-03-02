import time
import pytest
from selenium import webdriver

class TestLogin:
    @pytest.fixture(scope='session')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/11th_Class_2_3_2019_Automation_POM_Framework/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost/login.do")


    def test_login(self,test_launch_browser):
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("pwd").send_keys("manager")
        time.sleep(2)
        driver.find_element_by_xpath("//*[text()='Login ']").click()

    def test_logout(self,test_launch_browser):
        time.sleep(3)
        driver.find_element_by_xpath("//*[text()='Logout']").click()
        time.sleep(3)
        driver.quit()

# test_launch_browser()
# test_login(test_launch_browser)
# test_logout(test_launch_browser)