import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from config.config import Config
from utils.driver_factory import Utils


@pytest.fixture
def setup():
    browser = Config.Browser
    if browser == "Chrome":
        driver = webdriver.Chrome()
    driver.implicitly_wait(Config.wait_implicit)
    driver.get(Config.Base_url)
    yield driver
    driver.quit()

@allure.feature("Login Feature")
@allure.story("Login Validatiom")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(setup):
    driver = setup

    with allure.step("Initialize Login Page"):
        login = LoginPage(driver)


    with allure.step("Enter Username:"):
        login.get_user_name("standard_user")

    with allure.step("Enter Password:"):
        login.get_password("secret_sauce")

    with allure.step("Click Login"):
        login.login()

    with allure.step("Capture Screenshot"):
        Utils.take_screenshot(driver , "LoginPage")

    assert "inventory" in driver.current_url