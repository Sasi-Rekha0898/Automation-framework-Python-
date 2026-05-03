from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self , driver):
        self.driver = driver

    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    submit = (By.ID, "login-button")

    def get_user_name(self ,user):
        self.driver.find_element(*self.user_name).send_keys(user)

    def get_password(self , pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def login(self):
        self.driver.find_element(*self.submit).click()








