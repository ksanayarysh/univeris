from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from tests.models.locators import Locators
from tests.models.page import Page


class LoginPage(Page):
    def user_name(self):
        return self.driver.find_element(*Locators.LOGIN_NAME)

    def password(self):
        return self.driver.find_element(*Locators.PASSWORD)

    def submit(self):
        return self.driver.find_element(*Locators.SUBMIT)


    def fill_login(self, user_name):
        self.user_name().send_keys(user_name)

    def fill_password(self, password):
        self.password().send_keys(password)

    def press_submit(self):
        self.submit().click()

    def login(self, name, password):
        self.fill_login(name)
        self.fill_password(password)
        self.press_submit()

    def check_login(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.REAL_NAME))
            assert True
        except NoSuchElementException:
            assert False


