import configparser
import pytest
from selenium import webdriver

from tests.models.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def driver():
    wd = webdriver.Chrome()
    wd.maximize_window()
    yield wd
    wd.quit()


@pytest.fixture
def get_url():
    config = configparser.ConfigParser()
    config.read("config.db")
    return config['creds']["BASE_URL"]

@pytest.fixture
def get_user_name():
    config = configparser.ConfigParser()
    config.read("config.db")
    return config['creds']["USER_NAME"]

@pytest.fixture
def get_password():
    config = configparser.ConfigParser()
    config.read("config.db")
    return config['creds']["PASSWORD"]

@pytest.fixture
def open_login_page(driver, get_url):
    print(get_url)
    print(type(get_url))
    driver.get(get_url)
    return LoginPage(driver)
