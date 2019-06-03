from selenium.webdriver.common.by import By


class Locators:
    LOGIN_NAME = (By.ID, "UserName_I")
    PASSWORD = (By.ID, "Password_I")
    SUBMIT = (By.ID, "dxConfirm_CD")
    REAL_NAME = (By.PARTIAL_LINK_TEXT, "Ксения Владимировна")
