from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver=driver
        driver.set_page_load_timeout(50)

    __logout_link=(By.LINK_TEXT,"Logout")
    __task_tab=(By.XPATH,"//div[text()='Tasks']")

    def click_on_logout_link(self):
        self.driver.find_element(*self.__logout_link).click()

    def click_on_task_tab(self):
        self.driver.find_element(*self. __task_tab).click()