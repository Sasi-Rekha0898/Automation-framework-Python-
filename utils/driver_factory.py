import os
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class Utils:

    @staticmethod
    def take_screenshot(driver , name="screenshot"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        base_dir = os.getcwd()
        folder = os.path.join(base_dir, "Screenshots")

        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, file_name)
        driver.save_screenshot(file_path)


        allure.attach(
            driver.get_screenshot_as_png(),
            name=file_name ,
            attachment_type=allure.attachment_type.PNG

        )
        print(f"Screenshot Saved: {file_path}")


    @staticmethod
    def wait_for_element(driver, locator , timeout=Config.wait_explicit):
        wait = WebDriverWait(driver,timeout)
        wait.until(EC.visibility_of_element_located(locator))