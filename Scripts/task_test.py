from time import sleep

from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.task_page import TaskPage

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://demo.actitime.com")

login=LoginPage(driver)
login.set_username("admin")
login.set_password("manager")
login.click_login_button()

home=HomePage(driver)
home.click_on_task_tab()

task=TaskPage(driver)
task.click_on_add_new_button()
task.click_on_new_task()
sleep(5)
task.close_pop_up()
home.click_on_logout_link()
driver.quit()