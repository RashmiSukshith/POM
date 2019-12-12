from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://demo.actitime.com")

login=LoginPage(driver)
login.set_username("admin")
login.set_password("manager")
login.click_login_button()

home=HomePage(driver)
home.click_on_logout_link()
driver.quit()